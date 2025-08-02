_E='mandatory'
_D='read-write'
_C='enable'
_B='disable'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFPSServices,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFPSServices')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtFPSActivity_ObjectIdentity=ObjectIdentity
ctFPSActivity=_CtFPSActivity_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,15,1))
class _CtLookUpFwdActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_CtLookUpFwdActivity_Type.__name__=_A
_CtLookUpFwdActivity_Object=MibScalar
ctLookUpFwdActivity=_CtLookUpFwdActivity_Object((1,3,6,1,4,1,52,4,1,2,15,1,1),_CtLookUpFwdActivity_Type())
ctLookUpFwdActivity.setMaxAccess(_D)
if mibBuilder.loadTexts:ctLookUpFwdActivity.setStatus(_E)
class _CtINBActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_CtINBActivity_Type.__name__=_A
_CtINBActivity_Object=MibScalar
ctINBActivity=_CtINBActivity_Object((1,3,6,1,4,1,52,4,1,2,15,1,2),_CtINBActivity_Type())
ctINBActivity.setMaxAccess(_D)
if mibBuilder.loadTexts:ctINBActivity.setStatus(_E)
mibBuilder.exportSymbols('CT-FPS-SERVICES-MIB',**{'ctFPSActivity':ctFPSActivity,'ctLookUpFwdActivity':ctLookUpFwdActivity,'ctINBActivity':ctINBActivity})