_L='rbnAtmPvcOamNotifyGroup'
_K='rbnAtmPvcOamGroup'
_J='rbnAtmPvcOamStatusStateChange'
_I='rbnAtmPvcOamStatusVci'
_H='rbnAtmPvcOamStatusVpi'
_G='rbnAtmPvcOamStatusPort'
_F='rbnAtmPvcOamStatusSlot'
_E='rbnAtmPvcOamStatusState'
_D='not-accessible'
_C='Integer32'
_B='RBN-ATM-PVC-OAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnPort,RbnSlot=mibBuilder.importSymbols('RBN-TC','RbnPort','RbnSlot')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnAtmPvcOamMib=ModuleIdentity((1,3,6,1,4,1,2352,2,19))
if mibBuilder.loadTexts:rbnAtmPvcOamMib.setRevisions(('2002-11-13 00:00','2002-02-05 00:00'))
_RbnAtmPvcOamMibNotifications_ObjectIdentity=ObjectIdentity
rbnAtmPvcOamMibNotifications=_RbnAtmPvcOamMibNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,19,0))
_RbnAtmPvcOamMibObjects_ObjectIdentity=ObjectIdentity
rbnAtmPvcOamMibObjects=_RbnAtmPvcOamMibObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,19,1))
_RbnAtmPvcOamStatusTable_Object=MibTable
rbnAtmPvcOamStatusTable=_RbnAtmPvcOamStatusTable_Object((1,3,6,1,4,1,2352,2,19,1,1))
if mibBuilder.loadTexts:rbnAtmPvcOamStatusTable.setStatus(_A)
_RbnAtmPvcOamStatusEntry_Object=MibTableRow
rbnAtmPvcOamStatusEntry=_RbnAtmPvcOamStatusEntry_Object((1,3,6,1,4,1,2352,2,19,1,1,1))
rbnAtmPvcOamStatusEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:rbnAtmPvcOamStatusEntry.setStatus(_A)
_RbnAtmPvcOamStatusSlot_Type=RbnSlot
_RbnAtmPvcOamStatusSlot_Object=MibTableColumn
rbnAtmPvcOamStatusSlot=_RbnAtmPvcOamStatusSlot_Object((1,3,6,1,4,1,2352,2,19,1,1,1,1),_RbnAtmPvcOamStatusSlot_Type())
rbnAtmPvcOamStatusSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcOamStatusSlot.setStatus(_A)
_RbnAtmPvcOamStatusPort_Type=RbnPort
_RbnAtmPvcOamStatusPort_Object=MibTableColumn
rbnAtmPvcOamStatusPort=_RbnAtmPvcOamStatusPort_Object((1,3,6,1,4,1,2352,2,19,1,1,1,2),_RbnAtmPvcOamStatusPort_Type())
rbnAtmPvcOamStatusPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcOamStatusPort.setStatus(_A)
class _RbnAtmPvcOamStatusVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RbnAtmPvcOamStatusVpi_Type.__name__=_C
_RbnAtmPvcOamStatusVpi_Object=MibTableColumn
rbnAtmPvcOamStatusVpi=_RbnAtmPvcOamStatusVpi_Object((1,3,6,1,4,1,2352,2,19,1,1,1,3),_RbnAtmPvcOamStatusVpi_Type())
rbnAtmPvcOamStatusVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcOamStatusVpi.setStatus(_A)
class _RbnAtmPvcOamStatusVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnAtmPvcOamStatusVci_Type.__name__=_C
_RbnAtmPvcOamStatusVci_Object=MibTableColumn
rbnAtmPvcOamStatusVci=_RbnAtmPvcOamStatusVci_Object((1,3,6,1,4,1,2352,2,19,1,1,1,4),_RbnAtmPvcOamStatusVci_Type())
rbnAtmPvcOamStatusVci.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmPvcOamStatusVci.setStatus(_A)
class _RbnAtmPvcOamStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noOam',1),('oamUp',2),('oamDownLoopback',3),('oamDownAis',4),('oamDownRdi',5)))
_RbnAtmPvcOamStatusState_Type.__name__=_C
_RbnAtmPvcOamStatusState_Object=MibTableColumn
rbnAtmPvcOamStatusState=_RbnAtmPvcOamStatusState_Object((1,3,6,1,4,1,2352,2,19,1,1,1,5),_RbnAtmPvcOamStatusState_Type())
rbnAtmPvcOamStatusState.setMaxAccess('read-only')
if mibBuilder.loadTexts:rbnAtmPvcOamStatusState.setStatus(_A)
_RbnAtmPvcOamMibConformance_ObjectIdentity=ObjectIdentity
rbnAtmPvcOamMibConformance=_RbnAtmPvcOamMibConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,19,2))
_RbnAtmPvcOamCompliances_ObjectIdentity=ObjectIdentity
rbnAtmPvcOamCompliances=_RbnAtmPvcOamCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,19,2,1))
_RbnAtmPvcOamGroups_ObjectIdentity=ObjectIdentity
rbnAtmPvcOamGroups=_RbnAtmPvcOamGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,19,2,2))
rbnAtmPvcOamGroup=ObjectGroup((1,3,6,1,4,1,2352,2,19,2,2,1))
rbnAtmPvcOamGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:rbnAtmPvcOamGroup.setStatus(_A)
rbnAtmPvcOamStatusStateChange=NotificationType((1,3,6,1,4,1,2352,2,19,0,1))
rbnAtmPvcOamStatusStateChange.setObjects((_B,_E))
if mibBuilder.loadTexts:rbnAtmPvcOamStatusStateChange.setStatus(_A)
rbnAtmPvcOamNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,19,2,2,2))
rbnAtmPvcOamNotifyGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:rbnAtmPvcOamNotifyGroup.setStatus(_A)
rbnAtmPvcOamCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,19,2,1,1))
rbnAtmPvcOamCompliance.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:rbnAtmPvcOamCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnAtmPvcOamMib':rbnAtmPvcOamMib,'rbnAtmPvcOamMibNotifications':rbnAtmPvcOamMibNotifications,_J:rbnAtmPvcOamStatusStateChange,'rbnAtmPvcOamMibObjects':rbnAtmPvcOamMibObjects,'rbnAtmPvcOamStatusTable':rbnAtmPvcOamStatusTable,'rbnAtmPvcOamStatusEntry':rbnAtmPvcOamStatusEntry,_F:rbnAtmPvcOamStatusSlot,_G:rbnAtmPvcOamStatusPort,_H:rbnAtmPvcOamStatusVpi,_I:rbnAtmPvcOamStatusVci,_E:rbnAtmPvcOamStatusState,'rbnAtmPvcOamMibConformance':rbnAtmPvcOamMibConformance,'rbnAtmPvcOamCompliances':rbnAtmPvcOamCompliances,'rbnAtmPvcOamCompliance':rbnAtmPvcOamCompliance,'rbnAtmPvcOamGroups':rbnAtmPvcOamGroups,_K:rbnAtmPvcOamGroup,_L:rbnAtmPvcOamNotifyGroup})