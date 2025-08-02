_Z='tnVwmEcCardScalarsGroup'
_Y='tnVwmEcCardTableGroup'
_X='tnRedundancyDemeritTableGroup'
_W='tnControlCardTableGroup'
_V='tnControlCardScalarsGroup'
_U='tnVwmEcCardAttributeTotal'
_T='tnVwmEcCardClipOnId'
_S='tnVwmEcCardConnectTo'
_R='tnRedundancyDemeritValue'
_Q='tnRedundancyDemeritRaised'
_P='tnRedundancyDemeritName'
_O='tnControlCardActivityState'
_N='tnControlCardTotal'
_M='read-create'
_L='tnRedundancyDemeritId'
_K='Unsigned32'
_J='Integer32'
_I='SnmpAdminString'
_H='InterfaceIndexOrZero'
_G='tnSlotIndex'
_F='TROPIC-SLOT-MIB'
_E='tnShelfIndex'
_D='TROPIC-SHELF-MIB'
_C='read-only'
_B='TROPIC-CONTROLCARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
tnCardModules,tnControlCardMIB=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnCardModules','tnControlCardMIB')
tnShelfIndex,=mibBuilder.importSymbols(_D,_E)
tnSlotIndex,=mibBuilder.importSymbols(_F,_G)
tnControlCardMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,3,3))
if mibBuilder.loadTexts:tnControlCardMibModule.setRevisions(('2018-02-23 12:00','2017-07-07 12:00','2016-11-16 12:00','2014-09-04 12:00','2013-05-21 12:00'))
_TnControlCardConf_ObjectIdentity=ObjectIdentity
tnControlCardConf=_TnControlCardConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,3,1))
_TnControlCardGroups_ObjectIdentity=ObjectIdentity
tnControlCardGroups=_TnControlCardGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,3,1,1))
_TnControlCardCompliances_ObjectIdentity=ObjectIdentity
tnControlCardCompliances=_TnControlCardCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,3,1,2))
_TnControlCardObjs_ObjectIdentity=ObjectIdentity
tnControlCardObjs=_TnControlCardObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,3,2))
_TnControlCardTotal_Type=Integer32
_TnControlCardTotal_Object=MibScalar
tnControlCardTotal=_TnControlCardTotal_Object((1,3,6,1,4,1,7483,2,2,3,3,2,1),_TnControlCardTotal_Type())
tnControlCardTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tnControlCardTotal.setStatus(_A)
_TnControlCardTable_Object=MibTable
tnControlCardTable=_TnControlCardTable_Object((1,3,6,1,4,1,7483,2,2,3,3,2,2))
if mibBuilder.loadTexts:tnControlCardTable.setStatus(_A)
_TnControlCardEntry_Object=MibTableRow
tnControlCardEntry=_TnControlCardEntry_Object((1,3,6,1,4,1,7483,2,2,3,3,2,2,1))
tnControlCardEntry.setIndexNames((0,_D,_E),(0,_F,_G))
if mibBuilder.loadTexts:tnControlCardEntry.setStatus(_A)
class _TnControlCardActivityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('active',2),('inactive',3),('unequipped',4)))
_TnControlCardActivityState_Type.__name__=_J
_TnControlCardActivityState_Object=MibTableColumn
tnControlCardActivityState=_TnControlCardActivityState_Object((1,3,6,1,4,1,7483,2,2,3,3,2,2,1,1),_TnControlCardActivityState_Type())
tnControlCardActivityState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnControlCardActivityState.setStatus(_A)
_TnRedundancyDemeritTable_Object=MibTable
tnRedundancyDemeritTable=_TnRedundancyDemeritTable_Object((1,3,6,1,4,1,7483,2,2,3,3,2,3))
if mibBuilder.loadTexts:tnRedundancyDemeritTable.setStatus(_A)
_TnRedundancyDemeritEntry_Object=MibTableRow
tnRedundancyDemeritEntry=_TnRedundancyDemeritEntry_Object((1,3,6,1,4,1,7483,2,2,3,3,2,3,1))
tnRedundancyDemeritEntry.setIndexNames((0,_D,_E),(0,_F,_G),(0,_B,_L))
if mibBuilder.loadTexts:tnRedundancyDemeritEntry.setStatus(_A)
_TnRedundancyDemeritId_Type=Unsigned32
_TnRedundancyDemeritId_Object=MibTableColumn
tnRedundancyDemeritId=_TnRedundancyDemeritId_Object((1,3,6,1,4,1,7483,2,2,3,3,2,3,1,1),_TnRedundancyDemeritId_Type())
tnRedundancyDemeritId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnRedundancyDemeritId.setStatus(_A)
class _TnRedundancyDemeritName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnRedundancyDemeritName_Type.__name__=_I
_TnRedundancyDemeritName_Object=MibTableColumn
tnRedundancyDemeritName=_TnRedundancyDemeritName_Object((1,3,6,1,4,1,7483,2,2,3,3,2,3,1,2),_TnRedundancyDemeritName_Type())
tnRedundancyDemeritName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRedundancyDemeritName.setStatus(_A)
_TnRedundancyDemeritRaised_Type=TruthValue
_TnRedundancyDemeritRaised_Object=MibTableColumn
tnRedundancyDemeritRaised=_TnRedundancyDemeritRaised_Object((1,3,6,1,4,1,7483,2,2,3,3,2,3,1,3),_TnRedundancyDemeritRaised_Type())
tnRedundancyDemeritRaised.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRedundancyDemeritRaised.setStatus(_A)
_TnRedundancyDemeritValue_Type=Unsigned32
_TnRedundancyDemeritValue_Object=MibTableColumn
tnRedundancyDemeritValue=_TnRedundancyDemeritValue_Object((1,3,6,1,4,1,7483,2,2,3,3,2,3,1,4),_TnRedundancyDemeritValue_Type())
tnRedundancyDemeritValue.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRedundancyDemeritValue.setStatus(_A)
_TnVwmEcCardAttributeTotal_Type=Integer32
_TnVwmEcCardAttributeTotal_Object=MibScalar
tnVwmEcCardAttributeTotal=_TnVwmEcCardAttributeTotal_Object((1,3,6,1,4,1,7483,2,2,3,3,2,4),_TnVwmEcCardAttributeTotal_Type())
tnVwmEcCardAttributeTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVwmEcCardAttributeTotal.setStatus(_A)
_TnVwmEcCardTable_Object=MibTable
tnVwmEcCardTable=_TnVwmEcCardTable_Object((1,3,6,1,4,1,7483,2,2,3,3,2,5))
if mibBuilder.loadTexts:tnVwmEcCardTable.setStatus(_A)
_TnVwmEcCardEntry_Object=MibTableRow
tnVwmEcCardEntry=_TnVwmEcCardEntry_Object((1,3,6,1,4,1,7483,2,2,3,3,2,5,1))
tnVwmEcCardEntry.setIndexNames((0,_D,_E),(0,_F,_G))
if mibBuilder.loadTexts:tnVwmEcCardEntry.setStatus(_A)
class _TnVwmEcCardConnectTo_Type(InterfaceIndexOrZero):defaultValue=0
_TnVwmEcCardConnectTo_Type.__name__=_H
_TnVwmEcCardConnectTo_Object=MibTableColumn
tnVwmEcCardConnectTo=_TnVwmEcCardConnectTo_Object((1,3,6,1,4,1,7483,2,2,3,3,2,5,1,1),_TnVwmEcCardConnectTo_Type())
tnVwmEcCardConnectTo.setMaxAccess(_M)
if mibBuilder.loadTexts:tnVwmEcCardConnectTo.setStatus(_A)
class _TnVwmEcCardClipOnId_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnVwmEcCardClipOnId_Type.__name__=_K
_TnVwmEcCardClipOnId_Object=MibTableColumn
tnVwmEcCardClipOnId=_TnVwmEcCardClipOnId_Object((1,3,6,1,4,1,7483,2,2,3,3,2,5,1,2),_TnVwmEcCardClipOnId_Type())
tnVwmEcCardClipOnId.setMaxAccess(_M)
if mibBuilder.loadTexts:tnVwmEcCardClipOnId.setStatus(_A)
tnControlCardScalarsGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,3,1,1,1))
tnControlCardScalarsGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:tnControlCardScalarsGroup.setStatus(_A)
tnControlCardTableGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,3,1,1,2))
tnControlCardTableGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:tnControlCardTableGroup.setStatus(_A)
tnRedundancyDemeritTableGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,3,1,1,3))
tnRedundancyDemeritTableGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:tnRedundancyDemeritTableGroup.setStatus(_A)
tnVwmEcCardTableGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,3,1,1,4))
tnVwmEcCardTableGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:tnVwmEcCardTableGroup.setStatus(_A)
tnVwmEcCardScalarsGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,3,1,1,5))
tnVwmEcCardScalarsGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:tnVwmEcCardScalarsGroup.setStatus(_A)
tnControlCardCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,3,3,1,2,1))
tnControlCardCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:tnControlCardCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnControlCardMibModule':tnControlCardMibModule,'tnControlCardConf':tnControlCardConf,'tnControlCardGroups':tnControlCardGroups,_V:tnControlCardScalarsGroup,_W:tnControlCardTableGroup,_X:tnRedundancyDemeritTableGroup,_Y:tnVwmEcCardTableGroup,_Z:tnVwmEcCardScalarsGroup,'tnControlCardCompliances':tnControlCardCompliances,'tnControlCardCompliance':tnControlCardCompliance,'tnControlCardObjs':tnControlCardObjs,_N:tnControlCardTotal,'tnControlCardTable':tnControlCardTable,'tnControlCardEntry':tnControlCardEntry,_O:tnControlCardActivityState,'tnRedundancyDemeritTable':tnRedundancyDemeritTable,'tnRedundancyDemeritEntry':tnRedundancyDemeritEntry,_L:tnRedundancyDemeritId,_P:tnRedundancyDemeritName,_Q:tnRedundancyDemeritRaised,_R:tnRedundancyDemeritValue,_U:tnVwmEcCardAttributeTotal,'tnVwmEcCardTable':tnVwmEcCardTable,'tnVwmEcCardEntry':tnVwmEcCardEntry,_S:tnVwmEcCardConnectTo,_T:tnVwmEcCardClipOnId})