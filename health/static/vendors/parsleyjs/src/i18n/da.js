<<<<<<< HEAD
// Validation errors messages for Parsley
import Parsley from '../parsley';

Parsley.addMessages('da', {
  defaultMessage: "Indtast venligst en korrekt værdi.",
  type: {
    email:        "Indtast venligst en korrekt emailadresse.",
    url:          "Indtast venligst en korrekt internetadresse.",
    number:       "Indtast venligst et tal.",
    integer:      "Indtast venligst et heltal.",
    digits:       "Dette felt må kun bestå af tal.",
    alphanum:     "Dette felt skal indeholde både tal og bogstaver."
  },
  notblank:       "Dette felt må ikke være tomt.",
  required:       "Dette felt er påkrævet.",
  pattern:        "Ugyldig indtastning.",
  min:            "Dette felt skal indeholde et tal som er større end eller lig med %s.",
  max:            "Dette felt skal indeholde et tal som er mindre end eller lig med %s.",
  range:          "Dette felt skal indeholde et tal mellem %s og %s.",
  minlength:      "Indtast venligst mindst %s tegn.",
  maxlength:      "Dette felt kan højst indeholde %s tegn.",
  length:         "Længden af denne værdi er ikke korrekt. Værdien skal være mellem %s og %s tegn lang.",
  mincheck:       "Vælg mindst %s muligheder.",
  maxcheck:       "Vælg op til %s muligheder.",
  check:          "Vælg mellem %s og %s muligheder.",
  equalto:        "De to felter er ikke ens."
});

Parsley.setLocale('da');
=======
// Validation errors messages for Parsley
import Parsley from '../parsley';

Parsley.addMessages('da', {
  defaultMessage: "Indtast venligst en korrekt værdi.",
  type: {
    email:        "Indtast venligst en korrekt emailadresse.",
    url:          "Indtast venligst en korrekt internetadresse.",
    number:       "Indtast venligst et tal.",
    integer:      "Indtast venligst et heltal.",
    digits:       "Dette felt må kun bestå af tal.",
    alphanum:     "Dette felt skal indeholde både tal og bogstaver."
  },
  notblank:       "Dette felt må ikke være tomt.",
  required:       "Dette felt er påkrævet.",
  pattern:        "Ugyldig indtastning.",
  min:            "Dette felt skal indeholde et tal som er større end eller lig med %s.",
  max:            "Dette felt skal indeholde et tal som er mindre end eller lig med %s.",
  range:          "Dette felt skal indeholde et tal mellem %s og %s.",
  minlength:      "Indtast venligst mindst %s tegn.",
  maxlength:      "Dette felt kan højst indeholde %s tegn.",
  length:         "Længden af denne værdi er ikke korrekt. Værdien skal være mellem %s og %s tegn lang.",
  mincheck:       "Vælg mindst %s muligheder.",
  maxcheck:       "Vælg op til %s muligheder.",
  check:          "Vælg mellem %s og %s muligheder.",
  equalto:        "De to felter er ikke ens."
});

Parsley.setLocale('da');
>>>>>>> 5f91f3411245b1d3d2d998dbedeb8154265a24fb