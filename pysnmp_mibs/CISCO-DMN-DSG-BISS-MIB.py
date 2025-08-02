_D='Integer32'
_C='current'
_B='read-write'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
ciscoDSGBISS=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,38))
if mibBuilder.loadTexts:ciscoDSGBISS.setRevisions(('2010-08-02 07:00',))
class _BissMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mode1',1),('modeE',2)))
_BissMode_Type.__name__=_D
_BissMode_Object=MibScalar
bissMode=_BissMode_Object((1,3,6,1,4,1,1429,2,2,5,38,1),_BissMode_Type())
bissMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bissMode.setStatus(_C)
class _BissMode1SessionWord_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_BissMode1SessionWord_Type.__name__=_A
_BissMode1SessionWord_Object=MibScalar
bissMode1SessionWord=_BissMode1SessionWord_Object((1,3,6,1,4,1,1429,2,2,5,38,2),_BissMode1SessionWord_Type())
bissMode1SessionWord.setMaxAccess(_B)
if mibBuilder.loadTexts:bissMode1SessionWord.setStatus(_C)
class _BissModeESessionWord_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_BissModeESessionWord_Type.__name__=_A
_BissModeESessionWord_Object=MibScalar
bissModeESessionWord=_BissModeESessionWord_Object((1,3,6,1,4,1,1429,2,2,5,38,3),_BissModeESessionWord_Type())
bissModeESessionWord.setMaxAccess(_B)
if mibBuilder.loadTexts:bissModeESessionWord.setStatus(_C)
class _BissModeEInjectedId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_BissModeEInjectedId_Type.__name__=_A
_BissModeEInjectedId_Object=MibScalar
bissModeEInjectedId=_BissModeEInjectedId_Object((1,3,6,1,4,1,1429,2,2,5,38,4),_BissModeEInjectedId_Type())
bissModeEInjectedId.setMaxAccess(_B)
if mibBuilder.loadTexts:bissModeEInjectedId.setStatus(_C)
mibBuilder.exportSymbols('CISCO-DMN-DSG-BISS-MIB',**{'ciscoDSGBISS':ciscoDSGBISS,'bissMode':bissMode,'bissMode1SessionWord':bissMode1SessionWord,'bissModeESessionWord':bissModeESessionWord,'bissModeEInjectedId':bissModeEInjectedId})