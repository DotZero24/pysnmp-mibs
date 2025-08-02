_Y='csfFabricCrcErrorNotifsGroup'
_X='csfFabricCrcErrorNotifsInfoGroup'
_W='csfFabricCrcErrorNotifsControlGroup'
_V='csfFabricCrcErrorNotif'
_U='csfFabricCrcErrorNotifEnable'
_T='csfFabricUtilOutPeakTime'
_S='csfFabricUtilOutPeak'
_R='csfFabricUtilOut'
_Q='csfFabricUtilInPeakTime'
_P='csfFabricUtilInPeak'
_O='csfFabricUtilIn'
_N='csfFabricUtilBandwidth'
_M='csfFabricUtilDescr'
_L='accessible-for-notify'
_K='not-accessible'
_J='csfFabricUtilIndex'
_I='csfFabricUtilLinkType'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='csfFabricUtilGroup'
_E='csfFabricCrcErrorDescr'
_D='csfFabricCrcErrorEntPhysicalIndex'
_C='read-only'
_B='CISCO-SWITCH-FABRIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_G,'PhysicalIndex',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoSwitchFabricMIB=ModuleIdentity((1,3,6,1,4,1,9,9,803))
if mibBuilder.loadTexts:ciscoSwitchFabricMIB.setRevisions(('2014-07-30 00:00','2012-06-12 00:00'))
class CsfFabricLinkType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('qEngineFacingLcXbarLink',2),('fabricXbarLink',3),('fabricFacingLcXbarLink',4),('lcXbarInterLink',5),('fabricXbarInterLink',6),('centralXbarLink',7)))
class CsfPercentOrMinusOne(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_CiscoSwitchFabricMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSwitchFabricMIBNotifs=_CiscoSwitchFabricMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,803,0))
_CiscoSwitchFabricMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchFabricMIBObjects=_CiscoSwitchFabricMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,803,1))
_CsfFabricStatistics_ObjectIdentity=ObjectIdentity
csfFabricStatistics=_CsfFabricStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,803,1,1))
_CsfFabricUtilTable_Object=MibTable
csfFabricUtilTable=_CsfFabricUtilTable_Object((1,3,6,1,4,1,9,9,803,1,1,1))
if mibBuilder.loadTexts:csfFabricUtilTable.setStatus(_A)
_CsfFabricUtilEntry_Object=MibTableRow
csfFabricUtilEntry=_CsfFabricUtilEntry_Object((1,3,6,1,4,1,9,9,803,1,1,1,1))
csfFabricUtilEntry.setIndexNames((0,_G,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:csfFabricUtilEntry.setStatus(_A)
_CsfFabricUtilLinkType_Type=CsfFabricLinkType
_CsfFabricUtilLinkType_Object=MibTableColumn
csfFabricUtilLinkType=_CsfFabricUtilLinkType_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,1),_CsfFabricUtilLinkType_Type())
csfFabricUtilLinkType.setMaxAccess(_K)
if mibBuilder.loadTexts:csfFabricUtilLinkType.setStatus(_A)
_CsfFabricUtilIndex_Type=Unsigned32
_CsfFabricUtilIndex_Object=MibTableColumn
csfFabricUtilIndex=_CsfFabricUtilIndex_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,2),_CsfFabricUtilIndex_Type())
csfFabricUtilIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:csfFabricUtilIndex.setStatus(_A)
_CsfFabricUtilDescr_Type=SnmpAdminString
_CsfFabricUtilDescr_Object=MibTableColumn
csfFabricUtilDescr=_CsfFabricUtilDescr_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,3),_CsfFabricUtilDescr_Type())
csfFabricUtilDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilDescr.setStatus(_A)
_CsfFabricUtilBandwidth_Type=Unsigned32
_CsfFabricUtilBandwidth_Object=MibTableColumn
csfFabricUtilBandwidth=_CsfFabricUtilBandwidth_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,4),_CsfFabricUtilBandwidth_Type())
csfFabricUtilBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilBandwidth.setStatus(_A)
if mibBuilder.loadTexts:csfFabricUtilBandwidth.setUnits('gigabits per second')
_CsfFabricUtilIn_Type=CsfPercentOrMinusOne
_CsfFabricUtilIn_Object=MibTableColumn
csfFabricUtilIn=_CsfFabricUtilIn_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,5),_CsfFabricUtilIn_Type())
csfFabricUtilIn.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilIn.setStatus(_A)
_CsfFabricUtilInPeak_Type=CsfPercentOrMinusOne
_CsfFabricUtilInPeak_Object=MibTableColumn
csfFabricUtilInPeak=_CsfFabricUtilInPeak_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,6),_CsfFabricUtilInPeak_Type())
csfFabricUtilInPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilInPeak.setStatus(_A)
_CsfFabricUtilInPeakTime_Type=DateAndTime
_CsfFabricUtilInPeakTime_Object=MibTableColumn
csfFabricUtilInPeakTime=_CsfFabricUtilInPeakTime_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,7),_CsfFabricUtilInPeakTime_Type())
csfFabricUtilInPeakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilInPeakTime.setStatus(_A)
_CsfFabricUtilOut_Type=CsfPercentOrMinusOne
_CsfFabricUtilOut_Object=MibTableColumn
csfFabricUtilOut=_CsfFabricUtilOut_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,8),_CsfFabricUtilOut_Type())
csfFabricUtilOut.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilOut.setStatus(_A)
_CsfFabricUtilOutPeak_Type=CsfPercentOrMinusOne
_CsfFabricUtilOutPeak_Object=MibTableColumn
csfFabricUtilOutPeak=_CsfFabricUtilOutPeak_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,9),_CsfFabricUtilOutPeak_Type())
csfFabricUtilOutPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilOutPeak.setStatus(_A)
_CsfFabricUtilOutPeakTime_Type=DateAndTime
_CsfFabricUtilOutPeakTime_Object=MibTableColumn
csfFabricUtilOutPeakTime=_CsfFabricUtilOutPeakTime_Object((1,3,6,1,4,1,9,9,803,1,1,1,1,10),_CsfFabricUtilOutPeakTime_Type())
csfFabricUtilOutPeakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csfFabricUtilOutPeakTime.setStatus(_A)
_CsfNotifsControl_ObjectIdentity=ObjectIdentity
csfNotifsControl=_CsfNotifsControl_ObjectIdentity((1,3,6,1,4,1,9,9,803,1,2))
_CsfFabricCrcErrorNotifEnable_Type=TruthValue
_CsfFabricCrcErrorNotifEnable_Object=MibScalar
csfFabricCrcErrorNotifEnable=_CsfFabricCrcErrorNotifEnable_Object((1,3,6,1,4,1,9,9,803,1,2,1),_CsfFabricCrcErrorNotifEnable_Type())
csfFabricCrcErrorNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:csfFabricCrcErrorNotifEnable.setStatus(_A)
_CsfNotifsOnlyInfo_ObjectIdentity=ObjectIdentity
csfNotifsOnlyInfo=_CsfNotifsOnlyInfo_ObjectIdentity((1,3,6,1,4,1,9,9,803,1,3))
_CsfFabricCrcErrorEntPhysicalIndex_Type=PhysicalIndex
_CsfFabricCrcErrorEntPhysicalIndex_Object=MibScalar
csfFabricCrcErrorEntPhysicalIndex=_CsfFabricCrcErrorEntPhysicalIndex_Object((1,3,6,1,4,1,9,9,803,1,3,1),_CsfFabricCrcErrorEntPhysicalIndex_Type())
csfFabricCrcErrorEntPhysicalIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:csfFabricCrcErrorEntPhysicalIndex.setStatus(_A)
_CsfFabricCrcErrorDescr_Type=SnmpAdminString
_CsfFabricCrcErrorDescr_Object=MibScalar
csfFabricCrcErrorDescr=_CsfFabricCrcErrorDescr_Object((1,3,6,1,4,1,9,9,803,1,3,2),_CsfFabricCrcErrorDescr_Type())
csfFabricCrcErrorDescr.setMaxAccess(_L)
if mibBuilder.loadTexts:csfFabricCrcErrorDescr.setStatus(_A)
_CiscoSwitchFabricMIBConform_ObjectIdentity=ObjectIdentity
ciscoSwitchFabricMIBConform=_CiscoSwitchFabricMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,803,2))
_CsfSwitchFabricMIBCompliances_ObjectIdentity=ObjectIdentity
csfSwitchFabricMIBCompliances=_CsfSwitchFabricMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,803,2,1))
_CsfSwitchFabricMIBGroups_ObjectIdentity=ObjectIdentity
csfSwitchFabricMIBGroups=_CsfSwitchFabricMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,803,2,2))
csfFabricUtilGroup=ObjectGroup((1,3,6,1,4,1,9,9,803,2,2,1))
csfFabricUtilGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:csfFabricUtilGroup.setStatus(_A)
csfFabricCrcErrorNotifsControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,803,2,2,2))
csfFabricCrcErrorNotifsControlGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:csfFabricCrcErrorNotifsControlGroup.setStatus(_A)
csfFabricCrcErrorNotifsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,803,2,2,3))
csfFabricCrcErrorNotifsInfoGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:csfFabricCrcErrorNotifsInfoGroup.setStatus(_A)
csfFabricCrcErrorNotif=NotificationType((1,3,6,1,4,1,9,9,803,0,1))
csfFabricCrcErrorNotif.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:csfFabricCrcErrorNotif.setStatus(_A)
csfFabricCrcErrorNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,803,2,2,4))
csfFabricCrcErrorNotifsGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:csfFabricCrcErrorNotifsGroup.setStatus(_A)
csfSwitchFabricMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,803,2,1,1))
csfSwitchFabricMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:csfSwitchFabricMIBCompliance.setStatus('deprecated')
csfSwitchFabricMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,803,2,1,2))
csfSwitchFabricMIBCompliance1.setObjects(*((_B,_F),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:csfSwitchFabricMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CsfFabricLinkType':CsfFabricLinkType,'CsfPercentOrMinusOne':CsfPercentOrMinusOne,'ciscoSwitchFabricMIB':ciscoSwitchFabricMIB,'ciscoSwitchFabricMIBNotifs':ciscoSwitchFabricMIBNotifs,_V:csfFabricCrcErrorNotif,'ciscoSwitchFabricMIBObjects':ciscoSwitchFabricMIBObjects,'csfFabricStatistics':csfFabricStatistics,'csfFabricUtilTable':csfFabricUtilTable,'csfFabricUtilEntry':csfFabricUtilEntry,_I:csfFabricUtilLinkType,_J:csfFabricUtilIndex,_M:csfFabricUtilDescr,_N:csfFabricUtilBandwidth,_O:csfFabricUtilIn,_P:csfFabricUtilInPeak,_Q:csfFabricUtilInPeakTime,_R:csfFabricUtilOut,_S:csfFabricUtilOutPeak,_T:csfFabricUtilOutPeakTime,'csfNotifsControl':csfNotifsControl,_U:csfFabricCrcErrorNotifEnable,'csfNotifsOnlyInfo':csfNotifsOnlyInfo,_D:csfFabricCrcErrorEntPhysicalIndex,_E:csfFabricCrcErrorDescr,'ciscoSwitchFabricMIBConform':ciscoSwitchFabricMIBConform,'csfSwitchFabricMIBCompliances':csfSwitchFabricMIBCompliances,'csfSwitchFabricMIBCompliance':csfSwitchFabricMIBCompliance,'csfSwitchFabricMIBCompliance1':csfSwitchFabricMIBCompliance1,'csfSwitchFabricMIBGroups':csfSwitchFabricMIBGroups,_F:csfFabricUtilGroup,_W:csfFabricCrcErrorNotifsControlGroup,_X:csfFabricCrcErrorNotifsInfoGroup,_Y:csfFabricCrcErrorNotifsGroup})