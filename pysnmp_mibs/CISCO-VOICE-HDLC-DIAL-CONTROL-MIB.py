_J='cvHdlcCallHistoryGroup'
_I='cvHdlcCallHistorySessionTarget'
_H='cvHdlcCallHistoryLowerIfName'
_G='cvHdlcCallHistoryConnectionId'
_F='DisplayString'
_E='cCallHistoryIndex'
_D='CISCO-DIAL-CONTROL-MIB'
_C='read-only'
_B='CISCO-VOICE-HDLC-DIAL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_D,_E)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CvcGUid,=mibBuilder.importSymbols('CISCO-VOICE-DIAL-CONTROL-MIB','CvcGUid')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ciscoVoiceHdlcDialControlMIB=ModuleIdentity((1,3,6,1,4,1,9,10,37))
_CvhdlcdcMIBObjects_ObjectIdentity=ObjectIdentity
cvhdlcdcMIBObjects=_CvhdlcdcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,37,1))
_CvHdlcCallHistory_ObjectIdentity=ObjectIdentity
cvHdlcCallHistory=_CvHdlcCallHistory_ObjectIdentity((1,3,6,1,4,1,9,10,37,1,1))
_CvHdlcCallHistoryTable_Object=MibTable
cvHdlcCallHistoryTable=_CvHdlcCallHistoryTable_Object((1,3,6,1,4,1,9,10,37,1,1,1))
if mibBuilder.loadTexts:cvHdlcCallHistoryTable.setStatus(_A)
_CvHdlcCallHistoryEntry_Object=MibTableRow
cvHdlcCallHistoryEntry=_CvHdlcCallHistoryEntry_Object((1,3,6,1,4,1,9,10,37,1,1,1,1))
cvHdlcCallHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cvHdlcCallHistoryEntry.setStatus(_A)
_CvHdlcCallHistoryConnectionId_Type=CvcGUid
_CvHdlcCallHistoryConnectionId_Object=MibTableColumn
cvHdlcCallHistoryConnectionId=_CvHdlcCallHistoryConnectionId_Object((1,3,6,1,4,1,9,10,37,1,1,1,1,1),_CvHdlcCallHistoryConnectionId_Type())
cvHdlcCallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvHdlcCallHistoryConnectionId.setStatus(_A)
class _CvHdlcCallHistoryLowerIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CvHdlcCallHistoryLowerIfName_Type.__name__=_F
_CvHdlcCallHistoryLowerIfName_Object=MibTableColumn
cvHdlcCallHistoryLowerIfName=_CvHdlcCallHistoryLowerIfName_Object((1,3,6,1,4,1,9,10,37,1,1,1,1,2),_CvHdlcCallHistoryLowerIfName_Type())
cvHdlcCallHistoryLowerIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvHdlcCallHistoryLowerIfName.setStatus(_A)
_CvHdlcCallHistorySessionTarget_Type=DisplayString
_CvHdlcCallHistorySessionTarget_Object=MibTableColumn
cvHdlcCallHistorySessionTarget=_CvHdlcCallHistorySessionTarget_Object((1,3,6,1,4,1,9,10,37,1,1,1,1,3),_CvHdlcCallHistorySessionTarget_Type())
cvHdlcCallHistorySessionTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cvHdlcCallHistorySessionTarget.setStatus(_A)
_CvhdlcdcMIBConformance_ObjectIdentity=ObjectIdentity
cvhdlcdcMIBConformance=_CvhdlcdcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,37,3))
_CvhdlcdcMIBCompliances_ObjectIdentity=ObjectIdentity
cvhdlcdcMIBCompliances=_CvhdlcdcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,37,3,1))
_CvhdlcdcMIBGroups_ObjectIdentity=ObjectIdentity
cvhdlcdcMIBGroups=_CvhdlcdcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,37,3,2))
cvHdlcCallHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,10,37,3,2,1))
cvHdlcCallHistoryGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cvHdlcCallHistoryGroup.setStatus(_A)
cvhdlcdcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,37,3,1,1))
cvhdlcdcMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:cvhdlcdcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVoiceHdlcDialControlMIB':ciscoVoiceHdlcDialControlMIB,'cvhdlcdcMIBObjects':cvhdlcdcMIBObjects,'cvHdlcCallHistory':cvHdlcCallHistory,'cvHdlcCallHistoryTable':cvHdlcCallHistoryTable,'cvHdlcCallHistoryEntry':cvHdlcCallHistoryEntry,_G:cvHdlcCallHistoryConnectionId,_H:cvHdlcCallHistoryLowerIfName,_I:cvHdlcCallHistorySessionTarget,'cvhdlcdcMIBConformance':cvhdlcdcMIBConformance,'cvhdlcdcMIBCompliances':cvhdlcdcMIBCompliances,'cvhdlcdcMIBCompliance':cvhdlcdcMIBCompliance,'cvhdlcdcMIBGroups':cvhdlcdcMIBGroups,_J:cvHdlcCallHistoryGroup})