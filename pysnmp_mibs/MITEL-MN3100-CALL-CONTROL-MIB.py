_I='mitelCallCtrlDdiMappingErrorNotif'
_H='mitelCallCtrlFailedSeizeLineNotif'
_G='mitelCallCtrlFaultTblIndex'
_F='mitelCallCtrlFaultOccur'
_E='mitelCallCtrlFaultStatus'
_D='Integer32'
_C='read-only'
_B='MITEL-MN3100-CALL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelCallControl=ModuleIdentity((1,3,6,1,4,1,1027,4,9))
if mibBuilder.loadTexts:mitelCallControl.setRevisions(('2003-03-24 11:43','2002-04-02 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelIdentification_ObjectIdentity=ObjectIdentity
mitelIdentification=_MitelIdentification_ObjectIdentity((1,3,6,1,4,1,1027,1))
_MitelIdCallServers_ObjectIdentity=ObjectIdentity
mitelIdCallServers=_MitelIdCallServers_ObjectIdentity((1,3,6,1,4,1,1027,1,2))
_MitelIdCsIpera1000_ObjectIdentity=ObjectIdentity
mitelIdCsIpera1000=_MitelIdCsIpera1000_ObjectIdentity((1,3,6,1,4,1,1027,1,2,4))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelCallCtrlFaultTable_Object=MibTable
mitelCallCtrlFaultTable=_MitelCallCtrlFaultTable_Object((1,3,6,1,4,1,1027,4,9,1))
if mibBuilder.loadTexts:mitelCallCtrlFaultTable.setStatus(_A)
_MitelCallCtrlFaultEntry_Object=MibTableRow
mitelCallCtrlFaultEntry=_MitelCallCtrlFaultEntry_Object((1,3,6,1,4,1,1027,4,9,1,1))
mitelCallCtrlFaultEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:mitelCallCtrlFaultEntry.setStatus(_A)
_MitelCallCtrlFaultTblIndex_Type=Integer32
_MitelCallCtrlFaultTblIndex_Object=MibTableColumn
mitelCallCtrlFaultTblIndex=_MitelCallCtrlFaultTblIndex_Object((1,3,6,1,4,1,1027,4,9,1,1,1),_MitelCallCtrlFaultTblIndex_Type())
mitelCallCtrlFaultTblIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelCallCtrlFaultTblIndex.setStatus(_A)
class _MitelCallCtrlFaultId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mitelCallCtrlFailedSeizeLine',1),('mitelCallCtrlDdiMappingError',2)))
_MitelCallCtrlFaultId_Type.__name__=_D
_MitelCallCtrlFaultId_Object=MibTableColumn
mitelCallCtrlFaultId=_MitelCallCtrlFaultId_Object((1,3,6,1,4,1,1027,4,9,1,1,2),_MitelCallCtrlFaultId_Type())
mitelCallCtrlFaultId.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelCallCtrlFaultId.setStatus(_A)
class _MitelCallCtrlFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('set',1),('clear',2),('message',3)))
_MitelCallCtrlFaultStatus_Type.__name__=_D
_MitelCallCtrlFaultStatus_Object=MibTableColumn
mitelCallCtrlFaultStatus=_MitelCallCtrlFaultStatus_Object((1,3,6,1,4,1,1027,4,9,1,1,3),_MitelCallCtrlFaultStatus_Type())
mitelCallCtrlFaultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelCallCtrlFaultStatus.setStatus(_A)
_MitelCallCtrlFaultOccur_Type=Counter32
_MitelCallCtrlFaultOccur_Object=MibTableColumn
mitelCallCtrlFaultOccur=_MitelCallCtrlFaultOccur_Object((1,3,6,1,4,1,1027,4,9,1,1,4),_MitelCallCtrlFaultOccur_Type())
mitelCallCtrlFaultOccur.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelCallCtrlFaultOccur.setStatus(_A)
mitelCallCtrlFailedSeizeLineNotif=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,406))
mitelCallCtrlFailedSeizeLineNotif.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:mitelCallCtrlFailedSeizeLineNotif.setStatus(_A)
mitelCallCtrlDdiMappingErrorNotif=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,407))
mitelCallCtrlDdiMappingErrorNotif.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:mitelCallCtrlDdiMappingErrorNotif.setStatus(_A)
mitelIpera1000Notifications=NotificationGroup((1,3,6,1,4,1,1027,1,2,4,0))
mitelIpera1000Notifications.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:mitelIpera1000Notifications.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsIpera1000':mitelIdCsIpera1000,'mitelIpera1000Notifications':mitelIpera1000Notifications,_H:mitelCallCtrlFailedSeizeLineNotif,_I:mitelCallCtrlDdiMappingErrorNotif,'mitelProprietary':mitelProprietary,'mitelCallControl':mitelCallControl,'mitelCallCtrlFaultTable':mitelCallCtrlFaultTable,'mitelCallCtrlFaultEntry':mitelCallCtrlFaultEntry,_G:mitelCallCtrlFaultTblIndex,'mitelCallCtrlFaultId':mitelCallCtrlFaultId,_E:mitelCallCtrlFaultStatus,_F:mitelCallCtrlFaultOccur})