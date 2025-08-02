_M='cvEnabledLinkGroup'
_L='cvEnabledMacAddrGroup'
_K='cvEnabledLinkRemoteMacAddr'
_J='cvEnabledLinkVci'
_I='cvEnabledLinkVpiDlci'
_H='cvEnabledLinkInterfaceName'
_G='cvEnabledLinkType'
_F='cvEnabledDefaultMacAddr'
_E='cvEnabledLinkIndex'
_D='Integer32'
_C='read-only'
_B='CISCO-VOICE-ENABLED-LINK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ciscoVoiceEnabledLinkMIB=ModuleIdentity((1,3,6,1,4,1,9,10,53))
_CvenabledlinkMIBObjects_ObjectIdentity=ObjectIdentity
cvenabledlinkMIBObjects=_CvenabledlinkMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,53,1))
_CvEnabledLink_ObjectIdentity=ObjectIdentity
cvEnabledLink=_CvEnabledLink_ObjectIdentity((1,3,6,1,4,1,9,10,53,1,1))
_CvEnabledDefaultMacAddr_Type=MacAddress
_CvEnabledDefaultMacAddr_Object=MibScalar
cvEnabledDefaultMacAddr=_CvEnabledDefaultMacAddr_Object((1,3,6,1,4,1,9,10,53,1,1,1),_CvEnabledDefaultMacAddr_Type())
cvEnabledDefaultMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvEnabledDefaultMacAddr.setStatus(_A)
_CvEnabledLinkTable_Object=MibTable
cvEnabledLinkTable=_CvEnabledLinkTable_Object((1,3,6,1,4,1,9,10,53,1,1,2))
if mibBuilder.loadTexts:cvEnabledLinkTable.setStatus(_A)
_CvEnabledLinkEntry_Object=MibTableRow
cvEnabledLinkEntry=_CvEnabledLinkEntry_Object((1,3,6,1,4,1,9,10,53,1,1,2,1))
cvEnabledLinkEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cvEnabledLinkEntry.setStatus(_A)
class _CvEnabledLinkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483648))
_CvEnabledLinkIndex_Type.__name__=_D
_CvEnabledLinkIndex_Object=MibTableColumn
cvEnabledLinkIndex=_CvEnabledLinkIndex_Object((1,3,6,1,4,1,9,10,53,1,1,2,1,1),_CvEnabledLinkIndex_Type())
cvEnabledLinkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cvEnabledLinkIndex.setStatus(_A)
class _CvEnabledLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('atm',1),('framerelay',2)))
_CvEnabledLinkType_Type.__name__=_D
_CvEnabledLinkType_Object=MibTableColumn
cvEnabledLinkType=_CvEnabledLinkType_Object((1,3,6,1,4,1,9,10,53,1,1,2,1,2),_CvEnabledLinkType_Type())
cvEnabledLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvEnabledLinkType.setStatus(_A)
_CvEnabledLinkInterfaceName_Type=DisplayString
_CvEnabledLinkInterfaceName_Object=MibTableColumn
cvEnabledLinkInterfaceName=_CvEnabledLinkInterfaceName_Object((1,3,6,1,4,1,9,10,53,1,1,2,1,3),_CvEnabledLinkInterfaceName_Type())
cvEnabledLinkInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvEnabledLinkInterfaceName.setStatus(_A)
class _CvEnabledLinkVpiDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CvEnabledLinkVpiDlci_Type.__name__=_D
_CvEnabledLinkVpiDlci_Object=MibTableColumn
cvEnabledLinkVpiDlci=_CvEnabledLinkVpiDlci_Object((1,3,6,1,4,1,9,10,53,1,1,2,1,4),_CvEnabledLinkVpiDlci_Type())
cvEnabledLinkVpiDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:cvEnabledLinkVpiDlci.setStatus(_A)
class _CvEnabledLinkVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CvEnabledLinkVci_Type.__name__=_D
_CvEnabledLinkVci_Object=MibTableColumn
cvEnabledLinkVci=_CvEnabledLinkVci_Object((1,3,6,1,4,1,9,10,53,1,1,2,1,5),_CvEnabledLinkVci_Type())
cvEnabledLinkVci.setMaxAccess(_C)
if mibBuilder.loadTexts:cvEnabledLinkVci.setStatus(_A)
_CvEnabledLinkRemoteMacAddr_Type=MacAddress
_CvEnabledLinkRemoteMacAddr_Object=MibTableColumn
cvEnabledLinkRemoteMacAddr=_CvEnabledLinkRemoteMacAddr_Object((1,3,6,1,4,1,9,10,53,1,1,2,1,6),_CvEnabledLinkRemoteMacAddr_Type())
cvEnabledLinkRemoteMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvEnabledLinkRemoteMacAddr.setStatus(_A)
_CiscoVoiceEnabledLinkMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoVoiceEnabledLinkMIBNotificationPrefix=_CiscoVoiceEnabledLinkMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,53,2))
_CiscoVoiceEnabledLinkMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoVoiceEnabledLinkMIBNotifications=_CiscoVoiceEnabledLinkMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,53,2,0))
_CiscoVoiceEnabledlinkMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVoiceEnabledlinkMIBConformance=_CiscoVoiceEnabledlinkMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,53,3))
_CiscoVoiceEnabledlinkMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVoiceEnabledlinkMIBCompliances=_CiscoVoiceEnabledlinkMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,53,3,1))
_CiscoVoiceEnabledlinkMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVoiceEnabledlinkMIBGroups=_CiscoVoiceEnabledlinkMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,53,3,2))
cvEnabledMacAddrGroup=ObjectGroup((1,3,6,1,4,1,9,10,53,3,2,1))
cvEnabledMacAddrGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:cvEnabledMacAddrGroup.setStatus(_A)
cvEnabledLinkGroup=ObjectGroup((1,3,6,1,4,1,9,10,53,3,2,2))
cvEnabledLinkGroup.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cvEnabledLinkGroup.setStatus(_A)
ciscoVoiceEnabledlinkMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,53,3,1,1))
ciscoVoiceEnabledlinkMIBCompliance.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoVoiceEnabledlinkMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVoiceEnabledLinkMIB':ciscoVoiceEnabledLinkMIB,'cvenabledlinkMIBObjects':cvenabledlinkMIBObjects,'cvEnabledLink':cvEnabledLink,_F:cvEnabledDefaultMacAddr,'cvEnabledLinkTable':cvEnabledLinkTable,'cvEnabledLinkEntry':cvEnabledLinkEntry,_E:cvEnabledLinkIndex,_G:cvEnabledLinkType,_H:cvEnabledLinkInterfaceName,_I:cvEnabledLinkVpiDlci,_J:cvEnabledLinkVci,_K:cvEnabledLinkRemoteMacAddr,'ciscoVoiceEnabledLinkMIBNotificationPrefix':ciscoVoiceEnabledLinkMIBNotificationPrefix,'ciscoVoiceEnabledLinkMIBNotifications':ciscoVoiceEnabledLinkMIBNotifications,'ciscoVoiceEnabledlinkMIBConformance':ciscoVoiceEnabledlinkMIBConformance,'ciscoVoiceEnabledlinkMIBCompliances':ciscoVoiceEnabledlinkMIBCompliances,'ciscoVoiceEnabledlinkMIBCompliance':ciscoVoiceEnabledlinkMIBCompliance,'ciscoVoiceEnabledlinkMIBGroups':ciscoVoiceEnabledlinkMIBGroups,_L:cvEnabledMacAddrGroup,_M:cvEnabledLinkGroup})