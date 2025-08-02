_O='oaDevTrapsPortsNotificationGroup'
_N='oaDevTrapsPortsGroup'
_M='oaDevTrapsGenGroup'
_L='oaDevTrapsLinkUp'
_K='oaDevTrapsLinkDown'
_J='oaDevTrapsGenSupport'
_I='DisplayString'
_H='oaDevTrapsPortsIfAlias'
_G='oaDevTrapsPortsSlotPortNumber'
_F='oaDevTrapsPortsSlotNumber'
_E='read-only'
_D='oaDevTrapsPortsIfIndex'
_C='Integer32'
_B='current'
_A='OA-TRAP-MESSAGES-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
nbDeviceTrapMessages=ModuleIdentity((1,3,6,1,4,1,629,1,50,11,1,27))
if mibBuilder.loadTexts:nbDeviceTrapMessages.setRevisions(('2007-10-30 00:00',))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbDeviceConfig_ObjectIdentity=ObjectIdentity
nbDeviceConfig=_NbDeviceConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,11))
_NbDevGen_ObjectIdentity=ObjectIdentity
nbDevGen=_NbDevGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1))
_OaDevTrapsNotifications_ObjectIdentity=ObjectIdentity
oaDevTrapsNotifications=_OaDevTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,27,0))
_OaDevTrapsGen_ObjectIdentity=ObjectIdentity
oaDevTrapsGen=_OaDevTrapsGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,27,1))
class _OaDevTrapsGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OaDevTrapsGenSupport_Type.__name__=_C
_OaDevTrapsGenSupport_Object=MibScalar
oaDevTrapsGenSupport=_OaDevTrapsGenSupport_Object((1,3,6,1,4,1,629,1,50,11,1,27,1,1),_OaDevTrapsGenSupport_Type())
oaDevTrapsGenSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevTrapsGenSupport.setStatus(_B)
_OaDevTrapsPorts_ObjectIdentity=ObjectIdentity
oaDevTrapsPorts=_OaDevTrapsPorts_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,27,5))
_OaDevTrapsPortsTable_Object=MibTable
oaDevTrapsPortsTable=_OaDevTrapsPortsTable_Object((1,3,6,1,4,1,629,1,50,11,1,27,5,3))
if mibBuilder.loadTexts:oaDevTrapsPortsTable.setStatus(_B)
_OaDevTrapsPortsEntry_Object=MibTableRow
oaDevTrapsPortsEntry=_OaDevTrapsPortsEntry_Object((1,3,6,1,4,1,629,1,50,11,1,27,5,3,1))
oaDevTrapsPortsEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:oaDevTrapsPortsEntry.setStatus(_B)
class _OaDevTrapsPortsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OaDevTrapsPortsIfIndex_Type.__name__=_C
_OaDevTrapsPortsIfIndex_Object=MibTableColumn
oaDevTrapsPortsIfIndex=_OaDevTrapsPortsIfIndex_Object((1,3,6,1,4,1,629,1,50,11,1,27,5,3,1,1),_OaDevTrapsPortsIfIndex_Type())
oaDevTrapsPortsIfIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:oaDevTrapsPortsIfIndex.setStatus(_B)
class _OaDevTrapsPortsSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_OaDevTrapsPortsSlotNumber_Type.__name__=_C
_OaDevTrapsPortsSlotNumber_Object=MibTableColumn
oaDevTrapsPortsSlotNumber=_OaDevTrapsPortsSlotNumber_Object((1,3,6,1,4,1,629,1,50,11,1,27,5,3,1,2),_OaDevTrapsPortsSlotNumber_Type())
oaDevTrapsPortsSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevTrapsPortsSlotNumber.setStatus(_B)
class _OaDevTrapsPortsSlotPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_OaDevTrapsPortsSlotPortNumber_Type.__name__=_C
_OaDevTrapsPortsSlotPortNumber_Object=MibTableColumn
oaDevTrapsPortsSlotPortNumber=_OaDevTrapsPortsSlotPortNumber_Object((1,3,6,1,4,1,629,1,50,11,1,27,5,3,1,3),_OaDevTrapsPortsSlotPortNumber_Type())
oaDevTrapsPortsSlotPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevTrapsPortsSlotPortNumber.setStatus(_B)
class _OaDevTrapsPortsIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OaDevTrapsPortsIfAlias_Type.__name__=_I
_OaDevTrapsPortsIfAlias_Object=MibTableColumn
oaDevTrapsPortsIfAlias=_OaDevTrapsPortsIfAlias_Object((1,3,6,1,4,1,629,1,50,11,1,27,5,3,1,4),_OaDevTrapsPortsIfAlias_Type())
oaDevTrapsPortsIfAlias.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevTrapsPortsIfAlias.setStatus(_B)
_OaDevTrapsConformance_ObjectIdentity=ObjectIdentity
oaDevTrapsConformance=_OaDevTrapsConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,27,101))
_OaDevTrapsMIBCompliances_ObjectIdentity=ObjectIdentity
oaDevTrapsMIBCompliances=_OaDevTrapsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,27,101,1))
_OaDevTrapsMIBGroups_ObjectIdentity=ObjectIdentity
oaDevTrapsMIBGroups=_OaDevTrapsMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,27,101,2))
oaDevTrapsGenGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,27,101,2,1))
oaDevTrapsGenGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:oaDevTrapsGenGroup.setStatus(_B)
oaDevTrapsPortsGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,27,101,2,2))
oaDevTrapsPortsGroup.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:oaDevTrapsPortsGroup.setStatus(_B)
oaDevTrapsLinkDown=NotificationType((1,3,6,1,4,1,629,1,50,11,1,27,0,203))
oaDevTrapsLinkDown.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:oaDevTrapsLinkDown.setStatus(_B)
oaDevTrapsLinkUp=NotificationType((1,3,6,1,4,1,629,1,50,11,1,27,0,204))
oaDevTrapsLinkUp.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:oaDevTrapsLinkUp.setStatus(_B)
oaDevTrapsPortsNotificationGroup=NotificationGroup((1,3,6,1,4,1,629,1,50,11,1,27,101,2,3))
oaDevTrapsPortsNotificationGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:oaDevTrapsPortsNotificationGroup.setStatus(_B)
oaDevTrapsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,11,1,27,101,1,1))
oaDevTrapsMIBCompliance.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:oaDevTrapsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbDeviceConfig':nbDeviceConfig,'nbDevGen':nbDevGen,'nbDeviceTrapMessages':nbDeviceTrapMessages,'oaDevTrapsNotifications':oaDevTrapsNotifications,_K:oaDevTrapsLinkDown,_L:oaDevTrapsLinkUp,'oaDevTrapsGen':oaDevTrapsGen,_J:oaDevTrapsGenSupport,'oaDevTrapsPorts':oaDevTrapsPorts,'oaDevTrapsPortsTable':oaDevTrapsPortsTable,'oaDevTrapsPortsEntry':oaDevTrapsPortsEntry,_D:oaDevTrapsPortsIfIndex,_F:oaDevTrapsPortsSlotNumber,_G:oaDevTrapsPortsSlotPortNumber,_H:oaDevTrapsPortsIfAlias,'oaDevTrapsConformance':oaDevTrapsConformance,'oaDevTrapsMIBCompliances':oaDevTrapsMIBCompliances,'oaDevTrapsMIBCompliance':oaDevTrapsMIBCompliance,'oaDevTrapsMIBGroups':oaDevTrapsMIBGroups,_M:oaDevTrapsGenGroup,_N:oaDevTrapsPortsGroup,_O:oaDevTrapsPortsNotificationGroup})