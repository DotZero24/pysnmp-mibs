_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
mpe_arp,=mibBuilder.importSymbols('PDN-HEADER-MIB','mpe-arp')
SwitchState,VnidRange=mibBuilder.importSymbols('PDN-TC','SwitchState','VnidRange')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
class Bit32(Integer32):0
_MpePdnNetToMediaGenericMIBObjects_ObjectIdentity=ObjectIdentity
mpePdnNetToMediaGenericMIBObjects=_MpePdnNetToMediaGenericMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,27,1))
_MpePdnNetTo8023MediaParams_ObjectIdentity=ObjectIdentity
mpePdnNetTo8023MediaParams=_MpePdnNetTo8023MediaParams_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,27,1,1))
_MpePdnNetTo8023MediaParamsTable_Object=MibTable
mpePdnNetTo8023MediaParamsTable=_MpePdnNetTo8023MediaParamsTable_Object((1,3,6,1,4,1,1795,2,24,12,27,1,1,1))
if mibBuilder.loadTexts:mpePdnNetTo8023MediaParamsTable.setStatus(_A)
_MpePdnNetTo8023MediaParamsEntry_Object=MibTableRow
mpePdnNetTo8023MediaParamsEntry=_MpePdnNetTo8023MediaParamsEntry_Object((1,3,6,1,4,1,1795,2,24,12,27,1,1,1,1))
mpePdnNetTo8023MediaParamsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mpePdnNetTo8023MediaParamsEntry.setStatus(_A)
class _MpePdnNetTo8023MediaParamsCompEntryTimeout_Type(Integer32):defaultValue=20
_MpePdnNetTo8023MediaParamsCompEntryTimeout_Type.__name__=_B
_MpePdnNetTo8023MediaParamsCompEntryTimeout_Object=MibTableColumn
mpePdnNetTo8023MediaParamsCompEntryTimeout=_MpePdnNetTo8023MediaParamsCompEntryTimeout_Object((1,3,6,1,4,1,1795,2,24,12,27,1,1,1,1,1),_MpePdnNetTo8023MediaParamsCompEntryTimeout_Type())
mpePdnNetTo8023MediaParamsCompEntryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mpePdnNetTo8023MediaParamsCompEntryTimeout.setStatus(_A)
class _MpePdnNetTo8023MediaParamsIncompEntryTimeout_Type(Integer32):defaultValue=3
_MpePdnNetTo8023MediaParamsIncompEntryTimeout_Type.__name__=_B
_MpePdnNetTo8023MediaParamsIncompEntryTimeout_Object=MibTableColumn
mpePdnNetTo8023MediaParamsIncompEntryTimeout=_MpePdnNetTo8023MediaParamsIncompEntryTimeout_Object((1,3,6,1,4,1,1795,2,24,12,27,1,1,1,1,2),_MpePdnNetTo8023MediaParamsIncompEntryTimeout_Type())
mpePdnNetTo8023MediaParamsIncompEntryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mpePdnNetTo8023MediaParamsIncompEntryTimeout.setStatus(_A)
class _MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Type(Integer32):defaultValue=1
_MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Type.__name__=_B
_MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Object=MibTableColumn
mpePdnNetTo8023MediaParamsDefRouteEntryTimeout=_MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Object((1,3,6,1,4,1,1795,2,24,12,27,1,1,1,1,3),_MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Type())
mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setStatus(_A)
_MpePdnNetTo8023MediaConfig_ObjectIdentity=ObjectIdentity
mpePdnNetTo8023MediaConfig=_MpePdnNetTo8023MediaConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,27,1,2))
_MpePdnNetToMediaMIBTraps_ObjectIdentity=ObjectIdentity
mpePdnNetToMediaMIBTraps=_MpePdnNetToMediaMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,27,2))
mibBuilder.exportSymbols('PDN-MPE-ARP-MIB',**{'Bit32':Bit32,'mpePdnNetToMediaGenericMIBObjects':mpePdnNetToMediaGenericMIBObjects,'mpePdnNetTo8023MediaParams':mpePdnNetTo8023MediaParams,'mpePdnNetTo8023MediaParamsTable':mpePdnNetTo8023MediaParamsTable,'mpePdnNetTo8023MediaParamsEntry':mpePdnNetTo8023MediaParamsEntry,'mpePdnNetTo8023MediaParamsCompEntryTimeout':mpePdnNetTo8023MediaParamsCompEntryTimeout,'mpePdnNetTo8023MediaParamsIncompEntryTimeout':mpePdnNetTo8023MediaParamsIncompEntryTimeout,'mpePdnNetTo8023MediaParamsDefRouteEntryTimeout':mpePdnNetTo8023MediaParamsDefRouteEntryTimeout,'mpePdnNetTo8023MediaConfig':mpePdnNetTo8023MediaConfig,'mpePdnNetToMediaMIBTraps':mpePdnNetToMediaMIBTraps})