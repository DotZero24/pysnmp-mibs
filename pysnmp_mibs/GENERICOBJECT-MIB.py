_D='DisplayString'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardGeneric,=mibBuilder.importSymbols('BASIS-MIB','cardGeneric')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_GenericObjects_ObjectIdentity=ObjectIdentity
genericObjects=_GenericObjects_ObjectIdentity((1,3,6,1,4,1,351,110,2,8))
_GenericLineNum_Type=Integer32
_GenericLineNum_Object=MibScalar
genericLineNum=_GenericLineNum_Object((1,3,6,1,4,1,351,110,2,8,1),_GenericLineNum_Type())
genericLineNum.setMaxAccess(_A)
if mibBuilder.loadTexts:genericLineNum.setStatus(_B)
class _GenericLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,51,52,53,54,55,56,101,102,151,152,153,154)));namedValues=NamedValues(*(('dsx1ESF',1),('dsx1D4',2),('dsx1E1',3),('dsx1E1CRC',4),('dsx1E1MF',5),('dsx1E1CRC-MF',6),('dsx1E1clearchannel',7),('dsx3CbitParity',51),('dsx3g832-g804',52),('dsx3m13mode',53),('dsx3g751',54),('dsx3Unframed',55),('e3Unframed',56),('x21dte',101),('x21dce',102),('sonetSts3c',151),('sonetStm1',152),('sonetSts12c',153),('sonetStm4',154)))
_GenericLineType_Type.__name__=_C
_GenericLineType_Object=MibScalar
genericLineType=_GenericLineType_Object((1,3,6,1,4,1,351,110,2,8,2),_GenericLineType_Type())
genericLineType.setMaxAccess(_A)
if mibBuilder.loadTexts:genericLineType.setStatus(_B)
class _GenericTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_GenericTimeStamp_Type.__name__=_D
_GenericTimeStamp_Object=MibScalar
genericTimeStamp=_GenericTimeStamp_Object((1,3,6,1,4,1,351,110,2,8,3),_GenericTimeStamp_Type())
genericTimeStamp.setMaxAccess(_A)
if mibBuilder.loadTexts:genericTimeStamp.setStatus(_B)
mibBuilder.exportSymbols('GENERICOBJECT-MIB',**{'genericObjects':genericObjects,'genericLineNum':genericLineNum,'genericLineType':genericLineType,'genericTimeStamp':genericTimeStamp})