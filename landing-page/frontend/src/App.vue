<template>
  <div id="app" class="xd-app">
    <div class="blank-header xd-primary"><h1>XAI-Demonstrator <span class="beta-label"></span></h1></div>
    <header class="mainImage">
      <img class="logoaQ" v-bind:src="require('@/assets/alphaQuest_logo_rgbSmall.png')"/>
    </header>
    <main>
      <div id="select">
        <a v-for="useCase in useCases" :key="useCase.title" v-bind:href="useCase.route">
          <section class="xd-section xd-light">
            <img v-bind:src="useCase.logo" class="logo xd-secondary" :alt="useCase.title"/>
            <div class="description">
              <h3>{{ useCase.title }}</h3>
              <p>{{ useCase.description }}</p>
            </div>
            <img class="next" v-bind:src="require('@/assets/arrow-right.svg')"/>
          </section>
        </a>
      </div>

    </main>
    <FloatingInfoButton
        v-bind:info-text="infoText"
        v-bind:info-url="infoUrl"
        v-bind:link-label="linkLabel"/>
  </div>
</template>

<script>
import {FloatingInfoButton} from '@xai-demonstrator/xaidemo-ui';

export default {
  name: 'App',
  components: {
    FloatingInfoButton
  },
  data() {
    return {
      useCases: [
        {
          logo: require('@/assets/credit-control.png'),
          title: "Kreditwürdigkeit erkennen",
          description: "Entdecke, wie die KI die Kreditwürdigkeit anhand der Eingaben bestimmt!",
          route: "/sentiment/"
        },
        {
          logo: require('@/assets/inspection-eye.png'),
          title: "Gegenstände erkennen",
          description: "Finde heraus, woran die KI Gegenstände auf Bildern erkennt!",
          route: "/inspection/"
        }
      ],
      infoText: [
        {
          headline: "Was ist der XAI-Demonstrator?",
          paragraphs: [
            "Der XAI-Demonstrator ist eine App, die die Möglichkeiten von XAI durch interaktive Beispiele veranschaulicht."
          ]         
        },
        {
          headline: "Was ist XAI?",
          paragraphs: [
            "XAI steht für Explainable AI, also erklärende künstliche Intelligenz (KI). Darunter versteht man Methoden, " +
            "die die Vorhersagen der KI um erklärende Elemente erweitern."
          ]         
        },
        {
          headline: "Warum XAI?",
          paragraphs: [
            "Ein häufiges Hindernis bei der Nutzung von KI-Methoden ist der sogenannte Black Box-Charakter. " +
            "Dies bedeutet, dass die Nutzer nur das Ergebnis der Vorhersage erhalten, aber keine Informationen " +
            "oder Hinweise darauf, wie die KI zu dem Ergebnis gelangt ist. XAI ändert dies. " +
            "XAI liefert die Erklärungen zu den Vorhersagen und verbindet damit die Vorhersagequalität von KI mit " + 
            "der Nachvollziehbarkeit einer menschlichen Entscheidung."
          ]         
        },
        {
          headline: "Code Basis",
          paragraphs: [
            "Dieser XAI-Demonstrator ist eine Weiterentwicklung eines Projekts der Universität Ulm. "+ 
            "Der Code der Basis-App ist in folgendem"+
            " <a href='https://github.com/XAI-Demonstrator/xai-demonstrator'>GitHub-Repositorty</a> öffentlich einsehbar."
          ]         
        }            
      ],
      infoUrl: "https://www.alphaquest.de/",
      linkLabel: "Interesse geweckt? Besuche unsere Website! "
    }
  },
  created() {
    document.title = "XAI-Demonstrator"
  }
}
</script>

<style>

#app {
  display: flex;
}

.blank-header {
  height: 42px;

  padding-left: 12px;
  display: flex;
  align-items: center;

  font-family: 'Calibri Light', sans-serif;
  box-shadow: 0 4px 12px rgba(120, 120, 120, 0.4);
}

.beta-label {
  font-weight: 400;
  font-size: 18px;
  font-variant: all-small-caps;
}

header {
  padding: 10px;
  font-family: 'Calibri Light', sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  flex: 0;
  border-radius: 3px;
  box-shadow: 2px 2px 4px rgba(180, 180, 180, 0.5);
}

header h1, .blank-header h1 {
  color: #EBEBEB;
  padding: 0;
  margin: 0;
  font-weight: 400;
  font-size: 25px;
}
.mainImage {
  color: #FFFFFF;
}

header h3 {
  color: #EBEBEB;
  padding: 0;
  margin: 0;
  font-weight: 400;
}

#select {
  display: flex;
  flex-direction: column;
}

#select a {
  color: #323232;
  text-decoration: none;
  display: block;
}

#select a:visited {
  color: #323232;
}

#select section {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}

section img {
  flex-shrink: 0;
  flex-grow: 0;
}

section img.logo {
  height: 60px;
  width: 60px;
  border-radius: 100%;
}

section img.next {
  height: 50px;
  width: 15px;
}

.description {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-grow: 1;
  padding: 0 15px;
}

.description h3 {
  margin: 0;
  padding: 0;
  font-size: 1em;
  font-weight: 600;
}

.description p {
  margin: 0;
  font-size: 0.8em;
  padding: 5px 0 0;
  text-align: justify;
}

@media screen and (max-width: 450px) {

  #app {
    overflow: scroll;
    flex-direction: column;
  }

  .blank-header {
    top: 0;
    right: 0;
    left: 0;
    position: fixed;
    z-index: 1;
  }

  header {
    height: auto;
    min-height: 280px;
  }

  main {
    flex: 1;
  }

  #select a {
    margin-top: 12px;
  }

}


@media screen and (min-width: 450px) and (max-height: 650px) {
  #app {
    flex-direction: row;
    padding-right: 0;
  }

  .blank-header {
    top: 0;
    right: 0;
    left: 0;
    position: fixed;
    z-index: 1;
  }

  header {
    width: auto;
    min-width: 280px;
  }

  main {
    flex-shrink: 1;
    flex-grow: 1;
    overflow: scroll;
    padding-left: 8px;
    padding-right: 8px;
  }

  #select a {
    margin: 0 0 12px;
  }

}


@media screen and (min-width: 450px) and (min-height: 650px) {

  #app {
    flex-direction: column;
  }

  .blank-header {
    margin-bottom: 14px;
  }

  header {
    height: auto;
    min-height: 280px;
    margin-left: 4px;
    margin-right: 4px;
  }

  main {
    flex: 1;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  #select a {
    margin-top: 12px;
  }

}
</style>
