_L='cvFrCallHistoryGroup'
_K='cvFrCallHistorySessionTarget'
_J='cvFrCallHistoryLowerIfName'
_I='cvFrCallHistoryDlci'
_H='cvFrCallHistoryConnectionId'
_G='DisplayString'
_F='Integer32'
_E='cCallHistoryIndex'
_D='CISCO-DIAL-CONTROL-MIB'
_C='read-only'
_B='CISCO-VOICE-FR-DIAL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_D,_E)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CvcGUid,=mibBuilder.importSymbols('CISCO-VOICE-DIAL-CONTROL-MIB','CvcGUid')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
ciscoVoiceFrDialControlMIB=ModuleIdentity((1,3,6,1,4,1,9,10,36))
_CvfrdcMIBObjects_ObjectIdentity=ObjectIdentity
cvfrdcMIBObjects=_CvfrdcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,36,1))
_CvFrCallHistory_ObjectIdentity=ObjectIdentity
cvFrCallHistory=_CvFrCallHistory_ObjectIdentity((1,3,6,1,4,1,9,10,36,1,1))
_CvFrCallHistoryTable_Object=MibTable
cvFrCallHistoryTable=_CvFrCallHistoryTable_Object((1,3,6,1,4,1,9,10,36,1,1,1))
if mibBuilder.loadTexts:cvFrCallHistoryTable.setStatus(_A)
_CvFrCallHistoryEntry_Object=MibTableRow
cvFrCallHistoryEntry=_CvFrCallHistoryEntry_Object((1,3,6,1,4,1,9,10,36,1,1,1,1))
cvFrCallHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cvFrCallHistoryEntry.setStatus(_A)
_CvFrCallHistoryConnectionId_Type=CvcGUid
_CvFrCallHistoryConnectionId_Object=MibTableColumn
cvFrCallHistoryConnectionId=_CvFrCallHistoryConnectionId_Object((1,3,6,1,4,1,9,10,36,1,1,1,1,1),_CvFrCallHistoryConnectionId_Type())
cvFrCallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvFrCallHistoryConnectionId.setStatus(_A)
class _CvFrCallHistoryDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CvFrCallHistoryDlci_Type.__name__=_F
_CvFrCallHistoryDlci_Object=MibTableColumn
cvFrCallHistoryDlci=_CvFrCallHistoryDlci_Object((1,3,6,1,4,1,9,10,36,1,1,1,1,2),_CvFrCallHistoryDlci_Type())
cvFrCallHistoryDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:cvFrCallHistoryDlci.setStatus(_A)
class _CvFrCallHistoryLowerIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CvFrCallHistoryLowerIfName_Type.__name__=_G
_CvFrCallHistoryLowerIfName_Object=MibTableColumn
cvFrCallHistoryLowerIfName=_CvFrCallHistoryLowerIfName_Object((1,3,6,1,4,1,9,10,36,1,1,1,1,3),_CvFrCallHistoryLowerIfName_Type())
cvFrCallHistoryLowerIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvFrCallHistoryLowerIfName.setStatus(_A)
_CvFrCallHistorySessionTarget_Type=DisplayString
_CvFrCallHistorySessionTarget_Object=MibTableColumn
cvFrCallHistorySessionTarget=_CvFrCallHistorySessionTarget_Object((1,3,6,1,4,1,9,10,36,1,1,1,1,4),_CvFrCallHistorySessionTarget_Type())
cvFrCallHistorySessionTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cvFrCallHistorySessionTarget.setStatus(_A)
_CvfrdcMIBConformance_ObjectIdentity=ObjectIdentity
cvfrdcMIBConformance=_CvfrdcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,36,3))
_CvfrdcMIBCompliances_ObjectIdentity=ObjectIdentity
cvfrdcMIBCompliances=_CvfrdcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,36,3,1))
_CvfrdcMIBGroups_ObjectIdentity=ObjectIdentity
cvfrdcMIBGroups=_CvfrdcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,36,3,2))
cvFrCallHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,10,36,3,2,1))
cvFrCallHistoryGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cvFrCallHistoryGroup.setStatus(_A)
cvfrdcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,36,3,1,1))
cvfrdcMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:cvfrdcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVoiceFrDialControlMIB':ciscoVoiceFrDialControlMIB,'cvfrdcMIBObjects':cvfrdcMIBObjects,'cvFrCallHistory':cvFrCallHistory,'cvFrCallHistoryTable':cvFrCallHistoryTable,'cvFrCallHistoryEntry':cvFrCallHistoryEntry,_H:cvFrCallHistoryConnectionId,_I:cvFrCallHistoryDlci,_J:cvFrCallHistoryLowerIfName,_K:cvFrCallHistorySessionTarget,'cvfrdcMIBConformance':cvfrdcMIBConformance,'cvfrdcMIBCompliances':cvfrdcMIBCompliances,'cvfrdcMIBCompliance':cvfrdcMIBCompliance,'cvfrdcMIBGroups':cvfrdcMIBGroups,_L:cvFrCallHistoryGroup})