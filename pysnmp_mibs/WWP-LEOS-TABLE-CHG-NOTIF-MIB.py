_M='wwpLeosListenerRefreshCount'
_L='wwpLeosTableChgNotifIndexStr'
_K='wwpLeosTableChgNotifNumChanges'
_J='wwpLeosTableChgNotifOid'
_I='read-create'
_H='wwpLeosListenerIndex'
_G='wwpLeosTableChgNotifIndex'
_F='read-write'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='WWP-LEOS-TABLE-CHG-NOTIF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosTableChgNotifMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,9))
if mibBuilder.loadTexts:wwpLeosTableChgNotifMIB.setRevisions(('2002-03-12 00:00',))
_WwpLeosTableChgNotifMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosTableChgNotifMIBObjects=_WwpLeosTableChgNotifMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,9,1))
class _WwpLeosTableTrapNotifTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_WwpLeosTableTrapNotifTimer_Type.__name__=_D
_WwpLeosTableTrapNotifTimer_Object=MibScalar
wwpLeosTableTrapNotifTimer=_WwpLeosTableTrapNotifTimer_Object((1,3,6,1,4,1,6141,2,60,9,1,1),_WwpLeosTableTrapNotifTimer_Type())
wwpLeosTableTrapNotifTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosTableTrapNotifTimer.setStatus(_A)
class _WwpLeosListenerRefreshTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1000))
_WwpLeosListenerRefreshTimer_Type.__name__=_D
_WwpLeosListenerRefreshTimer_Object=MibScalar
wwpLeosListenerRefreshTimer=_WwpLeosListenerRefreshTimer_Object((1,3,6,1,4,1,6141,2,60,9,1,2),_WwpLeosListenerRefreshTimer_Type())
wwpLeosListenerRefreshTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosListenerRefreshTimer.setStatus(_A)
_WwpLeosTableChgNotifTable_Object=MibTable
wwpLeosTableChgNotifTable=_WwpLeosTableChgNotifTable_Object((1,3,6,1,4,1,6141,2,60,9,1,4))
if mibBuilder.loadTexts:wwpLeosTableChgNotifTable.setStatus(_A)
_WwpLeosTableChgNotifEntry_Object=MibTableRow
wwpLeosTableChgNotifEntry=_WwpLeosTableChgNotifEntry_Object((1,3,6,1,4,1,6141,2,60,9,1,4,1))
wwpLeosTableChgNotifEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:wwpLeosTableChgNotifEntry.setStatus(_A)
class _WwpLeosTableChgNotifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosTableChgNotifIndex_Type.__name__=_D
_WwpLeosTableChgNotifIndex_Object=MibTableColumn
wwpLeosTableChgNotifIndex=_WwpLeosTableChgNotifIndex_Object((1,3,6,1,4,1,6141,2,60,9,1,4,1,1),_WwpLeosTableChgNotifIndex_Type())
wwpLeosTableChgNotifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTableChgNotifIndex.setStatus(_A)
_WwpLeosTableChgNotifOid_Type=ObjectIdentifier
_WwpLeosTableChgNotifOid_Object=MibTableColumn
wwpLeosTableChgNotifOid=_WwpLeosTableChgNotifOid_Object((1,3,6,1,4,1,6141,2,60,9,1,4,1,2),_WwpLeosTableChgNotifOid_Type())
wwpLeosTableChgNotifOid.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTableChgNotifOid.setStatus(_A)
_WwpLeosTableChgNotifNumChanges_Type=Counter32
_WwpLeosTableChgNotifNumChanges_Object=MibTableColumn
wwpLeosTableChgNotifNumChanges=_WwpLeosTableChgNotifNumChanges_Object((1,3,6,1,4,1,6141,2,60,9,1,4,1,3),_WwpLeosTableChgNotifNumChanges_Type())
wwpLeosTableChgNotifNumChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTableChgNotifNumChanges.setStatus(_A)
_WwpLeosListenerTable_Object=MibTable
wwpLeosListenerTable=_WwpLeosListenerTable_Object((1,3,6,1,4,1,6141,2,60,9,1,5))
if mibBuilder.loadTexts:wwpLeosListenerTable.setStatus(_A)
_WwpLeosListenerEntry_Object=MibTableRow
wwpLeosListenerEntry=_WwpLeosListenerEntry_Object((1,3,6,1,4,1,6141,2,60,9,1,5,1))
wwpLeosListenerEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:wwpLeosListenerEntry.setStatus(_A)
class _WwpLeosListenerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosListenerIndex_Type.__name__=_D
_WwpLeosListenerIndex_Object=MibTableColumn
wwpLeosListenerIndex=_WwpLeosListenerIndex_Object((1,3,6,1,4,1,6141,2,60,9,1,5,1,1),_WwpLeosListenerIndex_Type())
wwpLeosListenerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosListenerIndex.setStatus(_A)
_WwpLeosListenerAddr_Type=DisplayString
_WwpLeosListenerAddr_Object=MibTableColumn
wwpLeosListenerAddr=_WwpLeosListenerAddr_Object((1,3,6,1,4,1,6141,2,60,9,1,5,1,2),_WwpLeosListenerAddr_Type())
wwpLeosListenerAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosListenerAddr.setStatus(_A)
_WwpLeosListenerResolvedIp_Type=IpAddress
_WwpLeosListenerResolvedIp_Object=MibTableColumn
wwpLeosListenerResolvedIp=_WwpLeosListenerResolvedIp_Object((1,3,6,1,4,1,6141,2,60,9,1,5,1,3),_WwpLeosListenerResolvedIp_Type())
wwpLeosListenerResolvedIp.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosListenerResolvedIp.setStatus(_A)
_WwpLeosListenerStatus_Type=RowStatus
_WwpLeosListenerStatus_Object=MibTableColumn
wwpLeosListenerStatus=_WwpLeosListenerStatus_Object((1,3,6,1,4,1,6141,2,60,9,1,5,1,4),_WwpLeosListenerStatus_Type())
wwpLeosListenerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosListenerStatus.setStatus(_A)
_WwpLeosTableChgNotif_ObjectIdentity=ObjectIdentity
wwpLeosTableChgNotif=_WwpLeosTableChgNotif_ObjectIdentity((1,3,6,1,4,1,6141,2,60,9,1,7))
class _WwpLeosTableChgNotifIndexStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpLeosTableChgNotifIndexStr_Type.__name__=_E
_WwpLeosTableChgNotifIndexStr_Object=MibScalar
wwpLeosTableChgNotifIndexStr=_WwpLeosTableChgNotifIndexStr_Object((1,3,6,1,4,1,6141,2,60,9,1,7,1),_WwpLeosTableChgNotifIndexStr_Type())
wwpLeosTableChgNotifIndexStr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTableChgNotifIndexStr.setStatus(_A)
class _WwpLeosListenerRefreshCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1000))
_WwpLeosListenerRefreshCount_Type.__name__=_D
_WwpLeosListenerRefreshCount_Object=MibScalar
wwpLeosListenerRefreshCount=_WwpLeosListenerRefreshCount_Object((1,3,6,1,4,1,6141,2,60,9,1,7,2),_WwpLeosListenerRefreshCount_Type())
wwpLeosListenerRefreshCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosListenerRefreshCount.setStatus(_A)
_WwpLeosTableChgNotifMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosTableChgNotifMIBNotificationPrefix=_WwpLeosTableChgNotifMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,9,2))
_WwpLeosTableChgNotifMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosTableChgNotifMIBNotifications=_WwpLeosTableChgNotifMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,9,2,0))
_WwpLeosTableChgNotifMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosTableChgNotifMIBConformance=_WwpLeosTableChgNotifMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,9,3))
_WwpLeosTableChgNotifMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosTableChgNotifMIBCompliances=_WwpLeosTableChgNotifMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,9,3,1))
_WwpLeosTableChgNotifMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosTableChgNotifMIBGroups=_WwpLeosTableChgNotifMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,9,3,2))
wwpLeosTableChgTrap=NotificationType((1,3,6,1,4,1,6141,2,60,9,2,0,1))
wwpLeosTableChgTrap.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:wwpLeosTableChgTrap.setStatus(_A)
wwpLeosTableRefreshTrap=NotificationType((1,3,6,1,4,1,6141,2,60,9,2,0,2))
wwpLeosTableRefreshTrap.setObjects((_B,_M))
if mibBuilder.loadTexts:wwpLeosTableRefreshTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'wwpLeosTableChgNotifMIB':wwpLeosTableChgNotifMIB,'wwpLeosTableChgNotifMIBObjects':wwpLeosTableChgNotifMIBObjects,'wwpLeosTableTrapNotifTimer':wwpLeosTableTrapNotifTimer,'wwpLeosListenerRefreshTimer':wwpLeosListenerRefreshTimer,'wwpLeosTableChgNotifTable':wwpLeosTableChgNotifTable,'wwpLeosTableChgNotifEntry':wwpLeosTableChgNotifEntry,_G:wwpLeosTableChgNotifIndex,_J:wwpLeosTableChgNotifOid,_K:wwpLeosTableChgNotifNumChanges,'wwpLeosListenerTable':wwpLeosListenerTable,'wwpLeosListenerEntry':wwpLeosListenerEntry,_H:wwpLeosListenerIndex,'wwpLeosListenerAddr':wwpLeosListenerAddr,'wwpLeosListenerResolvedIp':wwpLeosListenerResolvedIp,'wwpLeosListenerStatus':wwpLeosListenerStatus,'wwpLeosTableChgNotif':wwpLeosTableChgNotif,_L:wwpLeosTableChgNotifIndexStr,_M:wwpLeosListenerRefreshCount,'wwpLeosTableChgNotifMIBNotificationPrefix':wwpLeosTableChgNotifMIBNotificationPrefix,'wwpLeosTableChgNotifMIBNotifications':wwpLeosTableChgNotifMIBNotifications,'wwpLeosTableChgTrap':wwpLeosTableChgTrap,'wwpLeosTableRefreshTrap':wwpLeosTableRefreshTrap,'wwpLeosTableChgNotifMIBConformance':wwpLeosTableChgNotifMIBConformance,'wwpLeosTableChgNotifMIBCompliances':wwpLeosTableChgNotifMIBCompliances,'wwpLeosTableChgNotifMIBGroups':wwpLeosTableChgNotifMIBGroups})