_N='cvimMIBNotificationGroup'
_M='cvimMIBFaultGroup'
_L='cvimFaultActiveNotif'
_K='cvimFaultDescription'
_J='cvimNodeId'
_I='cvimFaultCode'
_H='cvimFaultSeverity'
_G='cvimFaultCreationTime'
_F='cvimFaultSource'
_E='cvimPodId'
_D='OctetString'
_C='not-accessible'
_B='current'
_A='CISCO-VIM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ciscoVimMIB=ModuleIdentity((1,3,6,1,4,1,9,9,855))
if mibBuilder.loadTexts:ciscoVimMIB.setRevisions(('2018-07-16 00:00',))
class CFaultSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('emergency',1),('critical',2),('major',3),('alert',4),('informational',5)))
class CFaultCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('resourceUsage',2),('resourceThreshold',3),('serviceFailure',4),('hardwareFailure',5),('networkConnectivity',6)))
_CiscoVimMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVimMIBNotifs=_CiscoVimMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,855,0))
_CiscoVimMIBFaults_ObjectIdentity=ObjectIdentity
ciscoVimMIBFaults=_CiscoVimMIBFaults_ObjectIdentity((1,3,6,1,4,1,9,9,855,1))
class _CvimPodId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CvimPodId_Type.__name__=_D
_CvimPodId_Object=MibScalar
cvimPodId=_CvimPodId_Object((1,3,6,1,4,1,9,9,855,1,1),_CvimPodId_Type())
cvimPodId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvimPodId.setStatus(_B)
_CvimFaultCreationTime_Type=DateAndTime
_CvimFaultCreationTime_Object=MibScalar
cvimFaultCreationTime=_CvimFaultCreationTime_Object((1,3,6,1,4,1,9,9,855,1,2),_CvimFaultCreationTime_Type())
cvimFaultCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvimFaultCreationTime.setStatus(_B)
class _CvimNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CvimNodeId_Type.__name__=_D
_CvimNodeId_Object=MibScalar
cvimNodeId=_CvimNodeId_Object((1,3,6,1,4,1,9,9,855,1,3),_CvimNodeId_Type())
cvimNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvimNodeId.setStatus(_B)
class _CvimFaultSource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,100))
_CvimFaultSource_Type.__name__=_D
_CvimFaultSource_Object=MibScalar
cvimFaultSource=_CvimFaultSource_Object((1,3,6,1,4,1,9,9,855,1,4),_CvimFaultSource_Type())
cvimFaultSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cvimFaultSource.setStatus(_B)
_CvimFaultSeverity_Type=CFaultSeverity
_CvimFaultSeverity_Object=MibScalar
cvimFaultSeverity=_CvimFaultSeverity_Object((1,3,6,1,4,1,9,9,855,1,5),_CvimFaultSeverity_Type())
cvimFaultSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cvimFaultSeverity.setStatus(_B)
_CvimFaultCode_Type=CFaultCode
_CvimFaultCode_Object=MibScalar
cvimFaultCode=_CvimFaultCode_Object((1,3,6,1,4,1,9,9,855,1,6),_CvimFaultCode_Type())
cvimFaultCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cvimFaultCode.setStatus(_B)
class _CvimFaultDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2048))
_CvimFaultDescription_Type.__name__=_D
_CvimFaultDescription_Object=MibScalar
cvimFaultDescription=_CvimFaultDescription_Object((1,3,6,1,4,1,9,9,855,1,7),_CvimFaultDescription_Type())
cvimFaultDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cvimFaultDescription.setStatus(_B)
_CiscoVimMIBConform_ObjectIdentity=ObjectIdentity
ciscoVimMIBConform=_CiscoVimMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,855,2))
_CiscoVimMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVimMIBCompliances=_CiscoVimMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,855,2,1))
_CiscoVimMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVimMIBGroups=_CiscoVimMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,855,2,2))
cvimMIBFaultGroup=ObjectGroup((1,3,6,1,4,1,9,9,855,2,2,1))
cvimMIBFaultGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:cvimMIBFaultGroup.setStatus(_B)
cvimFaultActiveNotif=NotificationType((1,3,6,1,4,1,9,9,855,0,1))
cvimFaultActiveNotif.setObjects(*((_A,_E),(_A,_G),(_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:cvimFaultActiveNotif.setStatus(_B)
cvimFaultClearNotif=NotificationType((1,3,6,1,4,1,9,9,855,0,2))
cvimFaultClearNotif.setObjects(*((_A,_E),(_A,_G),(_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:cvimFaultClearNotif.setStatus(_B)
cvimMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,855,2,2,2))
cvimMIBNotificationGroup.setObjects((_A,_L))
if mibBuilder.loadTexts:cvimMIBNotificationGroup.setStatus(_B)
cvimMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,855,2,1,1))
cvimMIBCompliance.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cvimMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CFaultSeverity':CFaultSeverity,'CFaultCode':CFaultCode,'ciscoVimMIB':ciscoVimMIB,'ciscoVimMIBNotifs':ciscoVimMIBNotifs,_L:cvimFaultActiveNotif,'cvimFaultClearNotif':cvimFaultClearNotif,'ciscoVimMIBFaults':ciscoVimMIBFaults,_E:cvimPodId,_G:cvimFaultCreationTime,_J:cvimNodeId,_F:cvimFaultSource,_H:cvimFaultSeverity,_I:cvimFaultCode,_K:cvimFaultDescription,'ciscoVimMIBConform':ciscoVimMIBConform,'ciscoVimMIBCompliances':ciscoVimMIBCompliances,'cvimMIBCompliance':cvimMIBCompliance,'ciscoVimMIBGroups':ciscoVimMIBGroups,_M:cvimMIBFaultGroup,_N:cvimMIBNotificationGroup})