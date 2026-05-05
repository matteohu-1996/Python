# Securetail — Sintesi Progetto

**Sistema di Video-Sorveglianza Intelligente Anti-Taccheggio**

---

**Studente:** [Nome Cognome]  
**Corso:** [Nome del corso]  
**Periodo:** 2 marzo – 23 aprile 2026 (8 settimane, ~300 ore)

---

## Obiettivo

Costruire un sistema che rilevi automaticamente tentativi di taccheggio in un negozio, facendo scattare un alert solo quando una persona entra davvero in una zona sensibile (ad esempio davanti a uno scaffale di prodotti costosi). Il sistema è pensato per:

- Funzionare in tempo reale (30 immagini al secondo) su un normale PC, senza schede grafiche costose
- Evitare i classici falsi allarmi causati da cambi di luce o ombre che si muovono
- Registrare automaticamente un breve video di 5 secondi prima dell'azione, per dare contesto all'operatore che revisiona l'evento
- Funzionare via internet, con il server che sta in cloud e la dashboard che si apre da qualsiasi browser

## Architettura

Il sistema è composto da 3 parti che lavorano insieme:

1. **Il programma che cattura il video** (sul PC del negozio, dove è collegata la webcam USB): prende le immagini dalla camera e le invia al server via internet.
2. **Il cervello del sistema** (sul server in cloud): riceve le immagini, le analizza con l'intelligenza artificiale per capire se c'è qualcosa di sospetto, registra gli eventi e salva tutto in un database.
3. **La dashboard web**: una pagina che si apre nel browser dove l'operatore può vedere le camere in diretta, rivedere i video degli eventi registrati, modificare le zone da sorvegliare e gestire gli utenti.

Il sistema è stato sviluppato e testato usando una webcam USB collegata al PC e trasmessa via internet al server. Tecnicamente il codice è predisposto anche per telecamere IP industriali (protocollo RTSP), ma questa modalità non è stata testata nella pratica.

## Come funziona l'intelligenza artificiale (pipeline a 2 livelli)

Il sistema usa un approccio "a filtri" che permette di ottenere buoni risultati senza sprecare risorse del computer. Funziona così:

**Livello 1 — Rilevazione del movimento**  
Un algoritmo molto leggero controlla ogni immagine confrontandola con l'ambiente "fermo" che ha memorizzato. Se non c'è nessun movimento (scaffale immobile, nessuno nel negozio), il sistema non fa nient'altro. Questo primo filtro scarta circa il 90% delle immagini, risparmiando moltissima energia.

**Livello 2 — Riconoscimento persona**  
Solo quando il primo livello rileva del movimento, si attiva il riconoscimento vero e proprio (una rete neurale chiamata YOLO11s-pose). Questa verifica:
- Se il movimento è davvero causato da una persona (non da un'ombra o una tenda che si muove)
- Dove si trova la persona rispetto allo scaffale sorvegliato
- Qual è la posizione del corpo (braccia, gambe, busto)

Se la persona è dentro la zona sorvegliata, il sistema registra un evento.

**Il video pre-evento di 5 secondi**  
Una caratteristica importante è che il sistema tiene sempre in memoria gli ultimi 5 secondi di video, pronto a salvarli quando scatta un allarme. Così nel video registrato si vede anche cosa è successo *prima* dell'azione, non solo durante. Per chi revisiona poi l'evento, questo fa la differenza tra capire o non capire la dinamica.

## Tecnologie utilizzate

| A cosa serve | Tecnologia |
|--------------|-----------|
| Analisi delle immagini | OpenCV (libreria di computer vision) + YOLOv11s-pose (intelligenza artificiale) |
| Comunicazione tra le parti del sistema | FastAPI (in Python) |
| Salvataggio dati | MySQL |
| Dashboard web | Streamlit |
| Cattura video | FFmpeg (standard per elaborazione video) |
| Ambiente server | Ubuntu Linux su un server cloud (Hostinger) |
| Compatibilità multi-sistema | Script Python che funziona su Windows, macOS e Linux |

## Risultati

| Metrica | Valore |
|---------|--------|
| Velocità di analisi | 30 immagini al secondo (fluido, tempo reale) |
| Tempo di riconoscimento persona | 27-30 millisecondi per immagine, su un normale processore i7 |
| Uso del processore | 35-45% in condizioni normali |
| Uso della memoria RAM | circa 1,2 GB |
| Falsi allarmi ambientali | Fortemente ridotti rispetto a un sistema basato solo sul movimento |

### Scenari testati

| Scenario | Comportamento atteso | Risultato ottenuto |
|----------|----------------------|---------------------|
| Sfarfallio delle luci (senza persone) | Nessun allarme | Bloccato 100% |
| Persona che cammina davanti allo scaffale | Allarme | Registrato 100% |
| Persona che passa ma fuori dalla zona sorvegliata | Nessun allarme | Bloccato 100% |
| Persona che si muove velocemente | Allarme | Registrato 95% |

## Funzionalità principali

- **Rilevazione intelligente a 2 livelli**: prima cerca il movimento, poi verifica se è una persona nella zona sorvegliata
- **Registrazione con contesto**: ogni evento include i 5 secondi precedenti
- **Salvataggio automatico** di video e immagini di anteprima
- **Dashboard web** con 4 sezioni: Home con statistiche, Monitor in diretta, Eventi registrati, Configurazione
- **Zone di interesse disegnabili**: l'utente può tracciare direttamente sullo schermo le aree da sorvegliare
- **Revisione degli eventi**: per ogni evento l'operatore può marcarlo come vero furto o falso allarme, così il sistema raccoglie statistiche di affidabilità
- **Gestione utenti a 2 livelli**: amministratore (può fare tutto) e viewer (può solo guardare, non può modificare o eliminare nulla)
- **Login con password cifrata** per la sicurezza degli accessi
- **Notifiche email automatiche** per gli eventi più gravi
- **Funziona da qualsiasi PC**: lo script di cattura video riconosce automaticamente Windows, macOS o Linux
- **Riavvio automatico**: se il sistema va in errore, si riavvia da solo
- **Conversione automatica dei video** in un formato compatibile con i browser moderni

## Limiti attuali del sistema

Il sistema è **funzionante e usabile** per dimostrazioni e test, ma **non è ancora pronto per essere venduto come prodotto finito**. Questi sono i principali limiti emersi durante lo sviluppo.

### Ci sono ancora dei falsi allarmi

Nonostante il doppio livello di controllo abbia ridotto molto i falsi allarmi ambientali, **non li elimina del tutto**. In alcune situazioni il sistema può far scattare un allarme anche quando non dovrebbe, ad esempio:

- Se c'è un manichino o una sagoma pubblicitaria umana nella scena, l'intelligenza artificiale può confonderli con una persona reale
- Riflessi marcati su vetrine o pavimenti lucidi possono creare l'illusione di una "persona virtuale"
- Un cliente che attraversa la zona sorvegliata per un motivo legittimo (senza intenzione di rubare) genera comunque l'allarme
- Quando ci sono molte persone vicine, il sistema può fare confusione

Per eliminare del tutto questi casi servirebbe un addestramento specifico dell'intelligenza artificiale su video di veri furti, e una fase di calibrazione per ogni singolo negozio.

### Il sistema richiede hardware più potente se si vuole alzare la qualità

Il sistema è stato progettato per funzionare su PC normali, il che è un vantaggio economico ma impone alcuni limiti.

**Camera testata**: tutti i test sono stati effettuati usando una webcam USB collegata al PC del "negozio" e trasmessa via rete TCP al server in cloud. Il codice è scritto in modo da supportare anche telecamere professionali di tipo IP (RTSP) — il formato usato nei sistemi di videosorveglianza commerciali — ma questa modalità non è mai stata testata nella pratica. Un'eventuale installazione reale in un negozio richiederebbe quindi una fase di testing con le telecamere effettive.

**Risoluzione della camera**: il sistema lavora bene con camere a risoluzione standard (fino a 1280×720). Se si volessero usare camere professionali 4K (ad alta definizione), il processore non ce la farebbe a stare al passo, la memoria RAM non basterebbe più e i tempi di analisi si triplicherebbero.

**Numero di camere**: è stato testato con una camera alla volta. Per aggiungere una seconda, terza o quarta camera (come servirebbe in un negozio reale) servirebbe raddoppiare o triplicare la potenza del computer, o aggiungere una scheda grafica dedicata.

**Prestazioni nel tempo**: in un caso isolato, dopo diverse ore di funzionamento continuato il server ha avuto un rallentamento importante. Non essendo capitato più di una volta non è stato possibile analizzarlo a fondo, ma suggerisce che un utilizzo intensivo 24 ore su 24 richiederebbe monitoraggio attento e ulteriori ottimizzazioni.

### La precisione della detection non è perfetta

L'intelligenza artificiale usata (YOLO11s-pose) è un modello general-purpose: è brava a riconoscere persone in situazioni generiche, ma non è stata addestrata specificamente per capire il contesto di un negozio o il gesto del furto. Questo si traduce in alcune situazioni in cui la detection fallisce:

- **Oggetti piccoli o distanti**: un prodotto tenuto in mano a 3-4 metri dalla camera può non essere visto
- **Persone parzialmente nascoste**: se qualcuno è dietro uno scaffale, il sistema fa più fatica a rilevarlo
- **Luci scarse o molto contrastate**: in condizioni di illuminazione difficile la precisione cala
- **Angolazioni strane della camera**: una camera montata al soffitto (vista dall'alto) funziona peggio di una camera frontale

Per avere una precisione migliore esistono modelli più grandi e potenti, ma consumano molte più risorse. In pratica: più precisione = più hardware = più costi.

### Il compromesso tra qualità e velocità

L'intero progetto è stato un continuo **bilanciamento tra due esigenze opposte**: da una parte riconoscere le persone e i gesti nel modo più preciso possibile; dall'altra farlo in tempo reale su un computer normale.

Alcune scelte tecniche riflettono questo compromesso:

- Le immagini vengono ridimensionate prima di essere analizzate: questo fa perdere un po' di dettaglio ma permette di analizzarle abbastanza velocemente da stare al passo con 30 immagini al secondo
- È stato scelto un modello di intelligenza artificiale "piccolo" invece di uno più grande: più veloce ma un po' meno preciso nei casi difficili
- È stata scelta una soglia intermedia per decidere se quello che si vede è davvero una persona: troppo alta farebbe sfuggire alcune persone vere, troppo bassa farebbe scattare più falsi allarmi

Un sistema veramente professionale richiederebbe hardware molto più potente (una workstation con scheda grafica dedicata di fascia alta, almeno 32 GB di RAM, camere industriali) e un budget significativamente maggiore.

## Conclusioni

Il progetto ha raggiunto gli obiettivi principali: il sistema funziona, sta girando su un server in cloud, monitora una webcam in diretta, registra automaticamente gli eventi sospetti e li mostra in una dashboard accessibile da qualsiasi browser. Gli operatori possono rivedere i video, marcarli come veri o falsi allarmi, e il sistema supporta più utenti con diversi livelli di permesso.

Il doppio livello di controllo (prima movimento, poi riconoscimento persona) ha dimostrato di funzionare: nei test eseguiti il sistema ha risposto correttamente al 95-100% dei casi, a seconda dello scenario.

Va però sottolineato che **Securetail si trova ancora in una fase sperimentale e prototipale**. Non è un prodotto pronto per essere venduto a un cliente finale. I limiti descritti sopra — falsi allarmi che ancora si verificano, necessità di hardware più potente per scalare, precisione che può migliorare, l'eterno compromesso tra qualità e velocità — dimostrano che c'è ancora strada da fare prima di avere un prodotto finito.

Quello che il progetto offre è **una base solida e funzionante su cui costruire e migliorare**: tutta l'architettura è già in piedi (cattura video, intelligenza artificiale, registrazione, dashboard, gestione permessi) e funzionante. Serve ora dedicare tempo al raffinamento: calibrare l'intelligenza artificiale su video reali di taccheggio, testare il sistema in condizioni d'uso prolungate, e personalizzarlo per le specifiche di ogni punto vendita che lo volesse adottare.

---

*23 aprile 2026*
