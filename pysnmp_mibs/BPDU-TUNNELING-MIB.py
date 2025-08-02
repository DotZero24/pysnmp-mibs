_H='swBPDUTunnelPortIndex'
_G='BPDU-TUNNELING-MIB'
_F='read-only'
_E='disabled'
_D='enabled'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
swBPDUTunnelMIB=ModuleIdentity((1,3,6,1,4,1,171,12,60))
_SwBPDUTunnelCtrl_ObjectIdentity=ObjectIdentity
swBPDUTunnelCtrl=_SwBPDUTunnelCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,60,1))
class _SwBPDUTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwBPDUTunnelState_Type.__name__=_B
_SwBPDUTunnelState_Object=MibScalar
swBPDUTunnelState=_SwBPDUTunnelState_Object((1,3,6,1,4,1,171,12,60,1,1),_SwBPDUTunnelState_Type())
swBPDUTunnelState.setMaxAccess(_C)
if mibBuilder.loadTexts:swBPDUTunnelState.setStatus(_A)
_SwBPDUTunnelInfo_ObjectIdentity=ObjectIdentity
swBPDUTunnelInfo=_SwBPDUTunnelInfo_ObjectIdentity((1,3,6,1,4,1,171,12,60,2))
_SwBPDUTunnelSTPMcastAddress_Type=MacAddress
_SwBPDUTunnelSTPMcastAddress_Object=MibScalar
swBPDUTunnelSTPMcastAddress=_SwBPDUTunnelSTPMcastAddress_Object((1,3,6,1,4,1,171,12,60,2,1),_SwBPDUTunnelSTPMcastAddress_Type())
swBPDUTunnelSTPMcastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swBPDUTunnelSTPMcastAddress.setStatus(_A)
_SwBPDUTunnelGVRPMcastAddress_Type=MacAddress
_SwBPDUTunnelGVRPMcastAddress_Object=MibScalar
swBPDUTunnelGVRPMcastAddress=_SwBPDUTunnelGVRPMcastAddress_Object((1,3,6,1,4,1,171,12,60,2,2),_SwBPDUTunnelGVRPMcastAddress_Type())
swBPDUTunnelGVRPMcastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swBPDUTunnelGVRPMcastAddress.setStatus(_A)
_SwBPDUTunnelMgmt_ObjectIdentity=ObjectIdentity
swBPDUTunnelMgmt=_SwBPDUTunnelMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,60,3))
_SwBPDUTunnelTable_Object=MibTable
swBPDUTunnelTable=_SwBPDUTunnelTable_Object((1,3,6,1,4,1,171,12,60,3,1))
if mibBuilder.loadTexts:swBPDUTunnelTable.setStatus(_A)
_SwBPDUTunnelEntry_Object=MibTableRow
swBPDUTunnelEntry=_SwBPDUTunnelEntry_Object((1,3,6,1,4,1,171,12,60,3,1,1))
swBPDUTunnelEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:swBPDUTunnelEntry.setStatus(_A)
class _SwBPDUTunnelPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwBPDUTunnelPortIndex_Type.__name__=_B
_SwBPDUTunnelPortIndex_Object=MibTableColumn
swBPDUTunnelPortIndex=_SwBPDUTunnelPortIndex_Object((1,3,6,1,4,1,171,12,60,3,1,1,1),_SwBPDUTunnelPortIndex_Type())
swBPDUTunnelPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swBPDUTunnelPortIndex.setStatus(_A)
class _SwBPDUTunnelPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('tunnel',2),('uplink',3)))
_SwBPDUTunnelPortType_Type.__name__=_B
_SwBPDUTunnelPortType_Object=MibTableColumn
swBPDUTunnelPortType=_SwBPDUTunnelPortType_Object((1,3,6,1,4,1,171,12,60,3,1,1,2),_SwBPDUTunnelPortType_Type())
swBPDUTunnelPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:swBPDUTunnelPortType.setStatus(_A)
class _SwBPDUTunnelSTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwBPDUTunnelSTPState_Type.__name__=_B
_SwBPDUTunnelSTPState_Object=MibTableColumn
swBPDUTunnelSTPState=_SwBPDUTunnelSTPState_Object((1,3,6,1,4,1,171,12,60,3,1,1,3),_SwBPDUTunnelSTPState_Type())
swBPDUTunnelSTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swBPDUTunnelSTPState.setStatus(_A)
class _SwBPDUTunnelGVRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwBPDUTunnelGVRPState_Type.__name__=_B
_SwBPDUTunnelGVRPState_Object=MibTableColumn
swBPDUTunnelGVRPState=_SwBPDUTunnelGVRPState_Object((1,3,6,1,4,1,171,12,60,3,1,1,4),_SwBPDUTunnelGVRPState_Type())
swBPDUTunnelGVRPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swBPDUTunnelGVRPState.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'swBPDUTunnelMIB':swBPDUTunnelMIB,'swBPDUTunnelCtrl':swBPDUTunnelCtrl,'swBPDUTunnelState':swBPDUTunnelState,'swBPDUTunnelInfo':swBPDUTunnelInfo,'swBPDUTunnelSTPMcastAddress':swBPDUTunnelSTPMcastAddress,'swBPDUTunnelGVRPMcastAddress':swBPDUTunnelGVRPMcastAddress,'swBPDUTunnelMgmt':swBPDUTunnelMgmt,'swBPDUTunnelTable':swBPDUTunnelTable,'swBPDUTunnelEntry':swBPDUTunnelEntry,_H:swBPDUTunnelPortIndex,'swBPDUTunnelPortType':swBPDUTunnelPortType,'swBPDUTunnelSTPState':swBPDUTunnelSTPState,'swBPDUTunnelGVRPState':swBPDUTunnelGVRPState})