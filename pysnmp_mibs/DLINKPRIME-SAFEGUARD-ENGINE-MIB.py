_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeSafeguardEngineMIB=ModuleIdentity((1,3,6,1,4,1,171,15,14))
if mibBuilder.loadTexts:dlinkPrimeSafeguardEngineMIB.setRevisions(('2014-04-26 00:00',))
_DpSafeguardEngineMIBNotif_ObjectIdentity=ObjectIdentity
dpSafeguardEngineMIBNotif=_DpSafeguardEngineMIBNotif_ObjectIdentity((1,3,6,1,4,1,171,15,14,0))
_DpSafeguardEngineMIBObjects_ObjectIdentity=ObjectIdentity
dpSafeguardEngineMIBObjects=_DpSafeguardEngineMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,14,1))
class _DpSafeguardEngineState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_DpSafeguardEngineState_Type.__name__=_A
_DpSafeguardEngineState_Object=MibScalar
dpSafeguardEngineState=_DpSafeguardEngineState_Object((1,3,6,1,4,1,171,15,14,1,1),_DpSafeguardEngineState_Type())
dpSafeguardEngineState.setMaxAccess('read-write')
if mibBuilder.loadTexts:dpSafeguardEngineState.setStatus('current')
_DpSafeguardEngineMIBConformance_ObjectIdentity=ObjectIdentity
dpSafeguardEngineMIBConformance=_DpSafeguardEngineMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,14,2))
mibBuilder.exportSymbols('DLINKPRIME-SAFEGUARD-ENGINE-MIB',**{'dlinkPrimeSafeguardEngineMIB':dlinkPrimeSafeguardEngineMIB,'dpSafeguardEngineMIBNotif':dpSafeguardEngineMIBNotif,'dpSafeguardEngineMIBObjects':dpSafeguardEngineMIBObjects,'dpSafeguardEngineState':dpSafeguardEngineState,'dpSafeguardEngineMIBConformance':dpSafeguardEngineMIBConformance})