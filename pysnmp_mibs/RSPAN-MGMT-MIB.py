_F='swRSPANVLANID'
_E='RSPAN-MGMT-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swRSPANMIB=ModuleIdentity((1,3,6,1,4,1,171,12,68))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwRSPANCtrl_ObjectIdentity=ObjectIdentity
swRSPANCtrl=_SwRSPANCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,68,1))
class _SwRSPANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwRSPANState_Type.__name__=_C
_SwRSPANState_Object=MibScalar
swRSPANState=_SwRSPANState_Object((1,3,6,1,4,1,171,12,68,1,1),_SwRSPANState_Type())
swRSPANState.setMaxAccess('read-write')
if mibBuilder.loadTexts:swRSPANState.setStatus(_A)
_SwRSPANInfo_ObjectIdentity=ObjectIdentity
swRSPANInfo=_SwRSPANInfo_ObjectIdentity((1,3,6,1,4,1,171,12,68,2))
class _SwRSPANMaxSupportedEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwRSPANMaxSupportedEntry_Type.__name__=_C
_SwRSPANMaxSupportedEntry_Object=MibScalar
swRSPANMaxSupportedEntry=_SwRSPANMaxSupportedEntry_Object((1,3,6,1,4,1,171,12,68,2,1),_SwRSPANMaxSupportedEntry_Type())
swRSPANMaxSupportedEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:swRSPANMaxSupportedEntry.setStatus(_A)
class _SwRSPANCurrentNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwRSPANCurrentNumEntries_Type.__name__=_C
_SwRSPANCurrentNumEntries_Object=MibScalar
swRSPANCurrentNumEntries=_SwRSPANCurrentNumEntries_Object((1,3,6,1,4,1,171,12,68,2,2),_SwRSPANCurrentNumEntries_Type())
swRSPANCurrentNumEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swRSPANCurrentNumEntries.setStatus(_A)
_SwRSPANMgmt_ObjectIdentity=ObjectIdentity
swRSPANMgmt=_SwRSPANMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,68,3))
_SwRSPANTable_Object=MibTable
swRSPANTable=_SwRSPANTable_Object((1,3,6,1,4,1,171,12,68,3,1))
if mibBuilder.loadTexts:swRSPANTable.setStatus(_A)
_SwRSPANEntry_Object=MibTableRow
swRSPANEntry=_SwRSPANEntry_Object((1,3,6,1,4,1,171,12,68,3,1,1))
swRSPANEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:swRSPANEntry.setStatus(_A)
_SwRSPANVLANID_Type=VlanId
_SwRSPANVLANID_Object=MibTableColumn
swRSPANVLANID=_SwRSPANVLANID_Object((1,3,6,1,4,1,171,12,68,3,1,1,1),_SwRSPANVLANID_Type())
swRSPANVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:swRSPANVLANID.setStatus(_A)
_SwRSPANSourceIngress_Type=PortList
_SwRSPANSourceIngress_Object=MibTableColumn
swRSPANSourceIngress=_SwRSPANSourceIngress_Object((1,3,6,1,4,1,171,12,68,3,1,1,2),_SwRSPANSourceIngress_Type())
swRSPANSourceIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:swRSPANSourceIngress.setStatus(_A)
_SwRSPANSourceEgress_Type=PortList
_SwRSPANSourceEgress_Object=MibTableColumn
swRSPANSourceEgress=_SwRSPANSourceEgress_Object((1,3,6,1,4,1,171,12,68,3,1,1,3),_SwRSPANSourceEgress_Type())
swRSPANSourceEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:swRSPANSourceEgress.setStatus(_A)
_SwRSPANRedirct_Type=PortList
_SwRSPANRedirct_Object=MibTableColumn
swRSPANRedirct=_SwRSPANRedirct_Object((1,3,6,1,4,1,171,12,68,3,1,1,4),_SwRSPANRedirct_Type())
swRSPANRedirct.setMaxAccess(_B)
if mibBuilder.loadTexts:swRSPANRedirct.setStatus(_A)
_SwRSPANRowStatus_Type=RowStatus
_SwRSPANRowStatus_Object=MibTableColumn
swRSPANRowStatus=_SwRSPANRowStatus_Object((1,3,6,1,4,1,171,12,68,3,1,1,5),_SwRSPANRowStatus_Type())
swRSPANRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swRSPANRowStatus.setStatus(_A)
_SwRSPANSrcMirrGroupID_Type=Integer32
_SwRSPANSrcMirrGroupID_Object=MibTableColumn
swRSPANSrcMirrGroupID=_SwRSPANSrcMirrGroupID_Object((1,3,6,1,4,1,171,12,68,3,1,1,6),_SwRSPANSrcMirrGroupID_Type())
swRSPANSrcMirrGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:swRSPANSrcMirrGroupID.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,'PortList':PortList,'swRSPANMIB':swRSPANMIB,'swRSPANCtrl':swRSPANCtrl,'swRSPANState':swRSPANState,'swRSPANInfo':swRSPANInfo,'swRSPANMaxSupportedEntry':swRSPANMaxSupportedEntry,'swRSPANCurrentNumEntries':swRSPANCurrentNumEntries,'swRSPANMgmt':swRSPANMgmt,'swRSPANTable':swRSPANTable,'swRSPANEntry':swRSPANEntry,_F:swRSPANVLANID,'swRSPANSourceIngress':swRSPANSourceIngress,'swRSPANSourceEgress':swRSPANSourceEgress,'swRSPANRedirct':swRSPANRedirct,'swRSPANRowStatus':swRSPANRowStatus,'swRSPANSrcMirrGroupID':swRSPANSrcMirrGroupID})