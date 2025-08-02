_M='mimosaEthernetSpeedChange'
_L='mimosaTempNormal'
_K='mimosaTempWarning'
_J='mimosaCriticalFault'
_I='DisplayString'
_H='ifIndex'
_G='IF-MIB'
_F='mimosaNewSpeed'
_E='mimosaOldSpeed'
_D='read-only'
_C='mimosaTrapMessage'
_B='current'
_A='MIMOSA-NETWORKS-BASE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
mimosa=ModuleIdentity((1,3,6,1,4,1,43356))
if mibBuilder.loadTexts:mimosa.setRevisions(('2020-12-01 00:00','2017-02-15 00:00','2015-05-17 00:00'))
_MimosaProduct_ObjectIdentity=ObjectIdentity
mimosaProduct=_MimosaProduct_ObjectIdentity((1,3,6,1,4,1,43356,1))
_MimosaHardware_ObjectIdentity=ObjectIdentity
mimosaHardware=_MimosaHardware_ObjectIdentity((1,3,6,1,4,1,43356,1,1))
_MimosaB5_ObjectIdentity=ObjectIdentity
mimosaB5=_MimosaB5_ObjectIdentity((1,3,6,1,4,1,43356,1,1,1))
_MimosaB5Lite_ObjectIdentity=ObjectIdentity
mimosaB5Lite=_MimosaB5Lite_ObjectIdentity((1,3,6,1,4,1,43356,1,1,2))
_MimosaA5_ObjectIdentity=ObjectIdentity
mimosaA5=_MimosaA5_ObjectIdentity((1,3,6,1,4,1,43356,1,1,3))
_MimosaC5_ObjectIdentity=ObjectIdentity
mimosaC5=_MimosaC5_ObjectIdentity((1,3,6,1,4,1,43356,1,1,4))
_MimosaB11_ObjectIdentity=ObjectIdentity
mimosaB11=_MimosaB11_ObjectIdentity((1,3,6,1,4,1,43356,1,1,5))
_MimosaB24_ObjectIdentity=ObjectIdentity
mimosaB24=_MimosaB24_ObjectIdentity((1,3,6,1,4,1,43356,1,1,6))
_MimosaC5c_ObjectIdentity=ObjectIdentity
mimosaC5c=_MimosaC5c_ObjectIdentity((1,3,6,1,4,1,43356,1,1,7))
_MimosaC5x_ObjectIdentity=ObjectIdentity
mimosaC5x=_MimosaC5x_ObjectIdentity((1,3,6,1,4,1,43356,1,1,8))
_MimosaSoftware_ObjectIdentity=ObjectIdentity
mimosaSoftware=_MimosaSoftware_ObjectIdentity((1,3,6,1,4,1,43356,1,2))
_MimosaMgmt_ObjectIdentity=ObjectIdentity
mimosaMgmt=_MimosaMgmt_ObjectIdentity((1,3,6,1,4,1,43356,2))
_MimosaTrap_ObjectIdentity=ObjectIdentity
mimosaTrap=_MimosaTrap_ObjectIdentity((1,3,6,1,4,1,43356,2,0))
_MimosaMib_ObjectIdentity=ObjectIdentity
mimosaMib=_MimosaMib_ObjectIdentity((1,3,6,1,4,1,43356,2,1))
_MimosaTrapMib_ObjectIdentity=ObjectIdentity
mimosaTrapMib=_MimosaTrapMib_ObjectIdentity((1,3,6,1,4,1,43356,2,1,1))
class _MimosaTrapMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MimosaTrapMessage_Type.__name__=_I
_MimosaTrapMessage_Object=MibScalar
mimosaTrapMessage=_MimosaTrapMessage_Object((1,3,6,1,4,1,43356,2,1,1,1),_MimosaTrapMessage_Type())
mimosaTrapMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:mimosaTrapMessage.setStatus(_B)
_MimosaOldSpeed_Type=Integer32
_MimosaOldSpeed_Object=MibScalar
mimosaOldSpeed=_MimosaOldSpeed_Object((1,3,6,1,4,1,43356,2,1,1,2),_MimosaOldSpeed_Type())
mimosaOldSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mimosaOldSpeed.setStatus(_B)
_MimosaNewSpeed_Type=Integer32
_MimosaNewSpeed_Object=MibScalar
mimosaNewSpeed=_MimosaNewSpeed_Object((1,3,6,1,4,1,43356,2,1,1,3),_MimosaNewSpeed_Type())
mimosaNewSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mimosaNewSpeed.setStatus(_B)
_MimosaWireless_ObjectIdentity=ObjectIdentity
mimosaWireless=_MimosaWireless_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2))
_MimosaMIBGroups_ObjectIdentity=ObjectIdentity
mimosaMIBGroups=_MimosaMIBGroups_ObjectIdentity((1,3,6,1,4,1,43356,2,3))
_MimosaConformanceGroup_ObjectIdentity=ObjectIdentity
mimosaConformanceGroup=_MimosaConformanceGroup_ObjectIdentity((1,3,6,1,4,1,43356,2,4))
mimosaTrapMIBGroup=ObjectGroup((1,3,6,1,4,1,43356,2,3,1))
mimosaTrapMIBGroup.setObjects(*((_A,_C),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:mimosaTrapMIBGroup.setStatus(_B)
mimosaCriticalFault=NotificationType((1,3,6,1,4,1,43356,2,0,1))
mimosaCriticalFault.setObjects((_A,_C))
if mibBuilder.loadTexts:mimosaCriticalFault.setStatus(_B)
mimosaTempWarning=NotificationType((1,3,6,1,4,1,43356,2,0,2))
mimosaTempWarning.setObjects((_A,_C))
if mibBuilder.loadTexts:mimosaTempWarning.setStatus(_B)
mimosaTempNormal=NotificationType((1,3,6,1,4,1,43356,2,0,3))
mimosaTempNormal.setObjects((_A,_C))
if mibBuilder.loadTexts:mimosaTempNormal.setStatus(_B)
mimosaEthernetSpeedChange=NotificationType((1,3,6,1,4,1,43356,2,0,4))
mimosaEthernetSpeedChange.setObjects(*((_G,_H),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:mimosaEthernetSpeedChange.setStatus(_B)
mimosaClientStatus=NotificationType((1,3,6,1,4,1,43356,2,0,5))
mimosaClientStatus.setObjects((_A,_C))
if mibBuilder.loadTexts:mimosaClientStatus.setStatus(_B)
mimosaGenericNotificationsGroup=NotificationGroup((1,3,6,1,4,1,43356,2,3,2))
mimosaGenericNotificationsGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:mimosaGenericNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'mimosa':mimosa,'mimosaProduct':mimosaProduct,'mimosaHardware':mimosaHardware,'mimosaB5':mimosaB5,'mimosaB5Lite':mimosaB5Lite,'mimosaA5':mimosaA5,'mimosaC5':mimosaC5,'mimosaB11':mimosaB11,'mimosaB24':mimosaB24,'mimosaC5c':mimosaC5c,'mimosaC5x':mimosaC5x,'mimosaSoftware':mimosaSoftware,'mimosaMgmt':mimosaMgmt,'mimosaTrap':mimosaTrap,_J:mimosaCriticalFault,_K:mimosaTempWarning,_L:mimosaTempNormal,_M:mimosaEthernetSpeedChange,'mimosaClientStatus':mimosaClientStatus,'mimosaMib':mimosaMib,'mimosaTrapMib':mimosaTrapMib,_C:mimosaTrapMessage,_E:mimosaOldSpeed,_F:mimosaNewSpeed,'mimosaWireless':mimosaWireless,'mimosaMIBGroups':mimosaMIBGroups,'mimosaTrapMIBGroup':mimosaTrapMIBGroup,'mimosaGenericNotificationsGroup':mimosaGenericNotificationsGroup,'mimosaConformanceGroup':mimosaConformanceGroup})