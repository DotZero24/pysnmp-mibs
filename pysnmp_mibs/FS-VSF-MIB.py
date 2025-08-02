_O='fsVsfMIBObjectsGroup'
_N='fsVsfApUptime'
_M='fsVsfPortPeerIfIndex'
_L='fsVsfPortState'
_K='fsVsfApIf'
_J='fsVsfDeviceStatus'
_I='fsVsfDeviceDescr'
_H='fsVsfDeviceMac'
_G='fsVsfApIndex'
_F='fsVsfPortIfIndex'
_E='fsVsfDeviceID'
_D='Integer32'
_C='read-only'
_B='FS-VSF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsVsfMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,140))
if mibBuilder.loadTexts:fsVsfMIB.setRevisions(('2015-06-01 00:00',))
_FsVsfMIBObjects_ObjectIdentity=ObjectIdentity
fsVsfMIBObjects=_FsVsfMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,140,1))
_FsVsfDeviceInfo_ObjectIdentity=ObjectIdentity
fsVsfDeviceInfo=_FsVsfDeviceInfo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,140,1,1))
_FsVsfDeviceTable_Object=MibTable
fsVsfDeviceTable=_FsVsfDeviceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,1,1))
if mibBuilder.loadTexts:fsVsfDeviceTable.setStatus(_A)
_FsVsfDeviceEntry_Object=MibTableRow
fsVsfDeviceEntry=_FsVsfDeviceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,1,1,1))
fsVsfDeviceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsVsfDeviceEntry.setStatus(_A)
_FsVsfDeviceID_Type=Integer32
_FsVsfDeviceID_Object=MibTableColumn
fsVsfDeviceID=_FsVsfDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,1,1,1,1),_FsVsfDeviceID_Type())
fsVsfDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfDeviceID.setStatus(_A)
_FsVsfDeviceMac_Type=MacAddress
_FsVsfDeviceMac_Object=MibTableColumn
fsVsfDeviceMac=_FsVsfDeviceMac_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,1,1,1,2),_FsVsfDeviceMac_Type())
fsVsfDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfDeviceMac.setStatus(_A)
_FsVsfDeviceDescr_Type=DisplayString
_FsVsfDeviceDescr_Object=MibTableColumn
fsVsfDeviceDescr=_FsVsfDeviceDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,1,1,1,3),_FsVsfDeviceDescr_Type())
fsVsfDeviceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfDeviceDescr.setStatus(_A)
class _FsVsfDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('recovery',2)))
_FsVsfDeviceStatus_Type.__name__=_D
_FsVsfDeviceStatus_Object=MibTableColumn
fsVsfDeviceStatus=_FsVsfDeviceStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,1,1,1,4),_FsVsfDeviceStatus_Type())
fsVsfDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfDeviceStatus.setStatus(_A)
_FsVsf_ObjectIdentity=ObjectIdentity
fsVsf=_FsVsf_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,140,1,2))
_FsVsfPortTable_Object=MibTable
fsVsfPortTable=_FsVsfPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,1))
if mibBuilder.loadTexts:fsVsfPortTable.setStatus(_A)
_FsVsfPortEntry_Object=MibTableRow
fsVsfPortEntry=_FsVsfPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,1,1))
fsVsfPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsVsfPortEntry.setStatus(_A)
_FsVsfPortIfIndex_Type=Integer32
_FsVsfPortIfIndex_Object=MibTableColumn
fsVsfPortIfIndex=_FsVsfPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,1,1,1),_FsVsfPortIfIndex_Type())
fsVsfPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfPortIfIndex.setStatus(_A)
_FsVsfApIf_Type=DisplayString
_FsVsfApIf_Object=MibTableColumn
fsVsfApIf=_FsVsfApIf_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,1,1,2),_FsVsfApIf_Type())
fsVsfApIf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfApIf.setStatus(_A)
class _FsVsfPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('down',1),('up',2),('ok',3),('disable',4),('aged',5)))
_FsVsfPortState_Type.__name__=_D
_FsVsfPortState_Object=MibTableColumn
fsVsfPortState=_FsVsfPortState_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,1,1,3),_FsVsfPortState_Type())
fsVsfPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfPortState.setStatus(_A)
_FsVsfPortPeerIfIndex_Type=Integer32
_FsVsfPortPeerIfIndex_Object=MibTableColumn
fsVsfPortPeerIfIndex=_FsVsfPortPeerIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,1,1,4),_FsVsfPortPeerIfIndex_Type())
fsVsfPortPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfPortPeerIfIndex.setStatus(_A)
_FsVsfApTable_Object=MibTable
fsVsfApTable=_FsVsfApTable_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,2))
if mibBuilder.loadTexts:fsVsfApTable.setStatus(_A)
_FsVsfApEntry_Object=MibTableRow
fsVsfApEntry=_FsVsfApEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,2,1))
fsVsfApEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsVsfApEntry.setStatus(_A)
_FsVsfApIndex_Type=Integer32
_FsVsfApIndex_Object=MibTableColumn
fsVsfApIndex=_FsVsfApIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,2,1,1),_FsVsfApIndex_Type())
fsVsfApIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfApIndex.setStatus(_A)
_FsVsfApUptime_Type=DisplayString
_FsVsfApUptime_Object=MibTableColumn
fsVsfApUptime=_FsVsfApUptime_Object((1,3,6,1,4,1,52642,1,1,10,2,140,1,2,2,1,2),_FsVsfApUptime_Type())
fsVsfApUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsfApUptime.setStatus(_A)
_FsVsfMIBConformance_ObjectIdentity=ObjectIdentity
fsVsfMIBConformance=_FsVsfMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,140,3))
_FsVsfMIBCompliances_ObjectIdentity=ObjectIdentity
fsVsfMIBCompliances=_FsVsfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,140,3,1))
_FsVsfMIBGroups_ObjectIdentity=ObjectIdentity
fsVsfMIBGroups=_FsVsfMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,140,3,2))
fsVsfMIBObjectsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,140,3,2,1))
fsVsfMIBObjectsGroup.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_G),(_B,_N)))
if mibBuilder.loadTexts:fsVsfMIBObjectsGroup.setStatus(_A)
fsVsfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,140,3,1,1))
fsVsfMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:fsVsfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsVsfMIB':fsVsfMIB,'fsVsfMIBObjects':fsVsfMIBObjects,'fsVsfDeviceInfo':fsVsfDeviceInfo,'fsVsfDeviceTable':fsVsfDeviceTable,'fsVsfDeviceEntry':fsVsfDeviceEntry,_E:fsVsfDeviceID,_H:fsVsfDeviceMac,_I:fsVsfDeviceDescr,_J:fsVsfDeviceStatus,'fsVsf':fsVsf,'fsVsfPortTable':fsVsfPortTable,'fsVsfPortEntry':fsVsfPortEntry,_F:fsVsfPortIfIndex,_K:fsVsfApIf,_L:fsVsfPortState,_M:fsVsfPortPeerIfIndex,'fsVsfApTable':fsVsfApTable,'fsVsfApEntry':fsVsfApEntry,_G:fsVsfApIndex,_N:fsVsfApUptime,'fsVsfMIBConformance':fsVsfMIBConformance,'fsVsfMIBCompliances':fsVsfMIBCompliances,'fsVsfMIBCompliance':fsVsfMIBCompliance,'fsVsfMIBGroups':fsVsfMIBGroups,_O:fsVsfMIBObjectsGroup})