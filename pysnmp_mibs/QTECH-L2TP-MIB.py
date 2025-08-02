_J='l2tpPrivateSessionExistTime'
_I='l2tpPrivateSessionVrfId'
_H='l2tpPrivateSessionRemoteIpAdd'
_G='l2tpPrivateSessionLocalIpAdd'
_F='l2tpPrivateLocalTunnelID'
_E='l2tpPrivateSessionIfIndex'
_D='read-only'
_C='Integer32'
_B='current'
_A='QTECH-L2TP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
qtechVPDNMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,112))
if mibBuilder.loadTexts:qtechVPDNMIB.setRevisions(('2011-02-17 00:00',))
_QtechL2TPSessionObjects_ObjectIdentity=ObjectIdentity
qtechL2TPSessionObjects=_QtechL2TPSessionObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,112,1))
_QtechL2TPSessionTable_Object=MibTable
qtechL2TPSessionTable=_QtechL2TPSessionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1))
if mibBuilder.loadTexts:qtechL2TPSessionTable.setStatus(_B)
_QtechL2TPSessionEntry_Object=MibTableRow
qtechL2TPSessionEntry=_QtechL2TPSessionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1))
qtechL2TPSessionEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:qtechL2TPSessionEntry.setStatus(_B)
class _L2tpPrivateSessionIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_L2tpPrivateSessionIfIndex_Type.__name__=_C
_L2tpPrivateSessionIfIndex_Object=MibTableColumn
l2tpPrivateSessionIfIndex=_L2tpPrivateSessionIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1,1),_L2tpPrivateSessionIfIndex_Type())
l2tpPrivateSessionIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpPrivateSessionIfIndex.setStatus(_B)
class _L2tpPrivateLocalTunnelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_L2tpPrivateLocalTunnelID_Type.__name__=_C
_L2tpPrivateLocalTunnelID_Object=MibTableColumn
l2tpPrivateLocalTunnelID=_L2tpPrivateLocalTunnelID_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1,2),_L2tpPrivateLocalTunnelID_Type())
l2tpPrivateLocalTunnelID.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpPrivateLocalTunnelID.setStatus(_B)
_L2tpPrivateSessionLocalIpAdd_Type=IpAddress
_L2tpPrivateSessionLocalIpAdd_Object=MibTableColumn
l2tpPrivateSessionLocalIpAdd=_L2tpPrivateSessionLocalIpAdd_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1,3),_L2tpPrivateSessionLocalIpAdd_Type())
l2tpPrivateSessionLocalIpAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpPrivateSessionLocalIpAdd.setStatus(_B)
_L2tpPrivateSessionRemoteIpAdd_Type=IpAddress
_L2tpPrivateSessionRemoteIpAdd_Object=MibTableColumn
l2tpPrivateSessionRemoteIpAdd=_L2tpPrivateSessionRemoteIpAdd_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1,4),_L2tpPrivateSessionRemoteIpAdd_Type())
l2tpPrivateSessionRemoteIpAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpPrivateSessionRemoteIpAdd.setStatus(_B)
class _L2tpPrivateSessionVrfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_L2tpPrivateSessionVrfId_Type.__name__=_C
_L2tpPrivateSessionVrfId_Object=MibTableColumn
l2tpPrivateSessionVrfId=_L2tpPrivateSessionVrfId_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1,5),_L2tpPrivateSessionVrfId_Type())
l2tpPrivateSessionVrfId.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpPrivateSessionVrfId.setStatus(_B)
class _L2tpPrivateSessionExistTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_L2tpPrivateSessionExistTime_Type.__name__=_C
_L2tpPrivateSessionExistTime_Object=MibTableColumn
l2tpPrivateSessionExistTime=_L2tpPrivateSessionExistTime_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1,6),_L2tpPrivateSessionExistTime_Type())
l2tpPrivateSessionExistTime.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpPrivateSessionExistTime.setStatus(_B)
class _L2tpPrivateSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sessionIdle',1),('sessionConnecting',2),('sessionEstablished',3),('sessionDisconnecting',4)))
_L2tpPrivateSessionStatus_Type.__name__=_C
_L2tpPrivateSessionStatus_Object=MibTableColumn
l2tpPrivateSessionStatus=_L2tpPrivateSessionStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,112,1,1,1,7),_L2tpPrivateSessionStatus_Type())
l2tpPrivateSessionStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:l2tpPrivateSessionStatus.setStatus(_B)
_QtechVPDNMonitor_ObjectIdentity=ObjectIdentity
qtechVPDNMonitor=_QtechVPDNMonitor_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,112,2))
_QtechVPDNMonitorTRAP_ObjectIdentity=ObjectIdentity
qtechVPDNMonitorTRAP=_QtechVPDNMonitorTRAP_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,112,2,1))
_QtechVPDNNotifications_ObjectIdentity=ObjectIdentity
qtechVPDNNotifications=_QtechVPDNNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,112,2,1,1))
qtechVPDNStart=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,112,2,1,1,1))
qtechVPDNStart.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:qtechVPDNStart.setStatus(_B)
qtechVPDNStop=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,112,2,1,1,2))
qtechVPDNStop.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:qtechVPDNStop.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechVPDNMIB':qtechVPDNMIB,'qtechL2TPSessionObjects':qtechL2TPSessionObjects,'qtechL2TPSessionTable':qtechL2TPSessionTable,'qtechL2TPSessionEntry':qtechL2TPSessionEntry,_E:l2tpPrivateSessionIfIndex,_F:l2tpPrivateLocalTunnelID,_G:l2tpPrivateSessionLocalIpAdd,_H:l2tpPrivateSessionRemoteIpAdd,_I:l2tpPrivateSessionVrfId,_J:l2tpPrivateSessionExistTime,'l2tpPrivateSessionStatus':l2tpPrivateSessionStatus,'qtechVPDNMonitor':qtechVPDNMonitor,'qtechVPDNMonitorTRAP':qtechVPDNMonitorTRAP,'qtechVPDNNotifications':qtechVPDNNotifications,'qtechVPDNStart':qtechVPDNStart,'qtechVPDNStop':qtechVPDNStop})