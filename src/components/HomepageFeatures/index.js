import clsx from 'clsx';
import Heading from '@theme/Heading';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const SUPPORTED_IMAGE_EXTENSIONS = ['png', 'jpg', 'webp', 'svg'];

function hasSupportedImageFormat(imagePath) {
  const extension = imagePath.split('.').pop()?.toLowerCase();
  return SUPPORTED_IMAGE_EXTENSIONS.includes(extension);
}

const FeatureList = [
  {
    title: 'Programación',
    image: '/img/programa.webp',
    description: (
      <>
        Este curso fue diseñado desde cero para ser fácilmente asequible y comprensible para todos. No requiere conocimientos previos de estadística o programación.
      </>
    ),
  },
  {
    title: 'Data Science',
    image: '/img/programacionf.png',
    description: (
      <>
        Se enfoca en la aplicación de la estadística en la investigación médica, y cubre los conceptos y técnicas estadísticas más relevantes para el análisis de datos en este campo.
      </>
    ),
  },
  {
    title: 'Desarrollo Continuo',
    image: '/img/undraw_docusaurus_react.svg',
    description: (
      <>
        Esta en constante desarrollo, y se irán agregando nuevos contenidos y recursos a medida que se avance en el curso. Se anima a los estudiantes a participar activamente en el curso, compartiendo sus experiencias y sugerencias.
      </>
    ),
  },
];

function Feature({image, title, description}) {
  if (!hasSupportedImageFormat(image)) {
    return null;
  }

  const imageUrl = useBaseUrl(image);

  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <img className={styles.featureSvg} src={imageUrl} alt={title} />
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
