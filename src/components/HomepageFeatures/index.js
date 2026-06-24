import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Programación',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Este curso fue diseñado desde cero para ser fácilmente asequible y comprensible para todos. No requiere conocimientos previos de estadística o programación.
      </>
    ),
  },
  {
    title: 'Data Science',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Se enfoca en la aplicación de la estadística en la investigación médica, y cubre los conceptos y técnicas estadísticas más relevantes para el análisis de datos en este campo.
      </>
    ),
  },
  {
    title: 'Desarrollo Continuo',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Esta en constante desarrollo, y se irán agregando nuevos contenidos y recursos a medida que se avance en el curso. Se anima a los estudiantes a participar activamente en el curso, compartiendo sus experiencias y sugerencias.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
