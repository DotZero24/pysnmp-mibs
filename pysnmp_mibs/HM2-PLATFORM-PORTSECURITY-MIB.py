_R='hm2AgentPortSecurityLastDiscardedMAC'
_Q='hm2AgentPortSecurityStaticIpAddress'
_P='hm2AgentPortSecurityStaticIpVLANId'
_O='hm2AgentPortSecurityStaticMACAddress'
_N='hm2AgentPortSecurityStaticVLANId'
_M='hm2AgentPortSecurityDynamicMACAddress'
_L='hm2AgentPortSecurityDynamicVLANId'
_K='TruthValue'
_J='Integer32'
_I='DisplayString'
_H='Unsigned32'
_G='HmEnabledStatus'
_F='ifIndex'
_E='IF-MIB'
_D='HM2-PLATFORM-PORTSECURITY-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2PlatformMibs=mibBuilder.importSymbols('HM2-TC-MIB',_G,'hm2PlatformMibs')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention',_K)
hm2PlatformPortSecurity=ModuleIdentity((1,3,6,1,4,1,248,12,20))
if mibBuilder.loadTexts:hm2PlatformPortSecurity.setRevisions(('2011-07-12 00:00',))
_Hm2AgentPortSecurityGroup_ObjectIdentity=ObjectIdentity
hm2AgentPortSecurityGroup=_Hm2AgentPortSecurityGroup_ObjectIdentity((1,3,6,1,4,1,248,12,20,1))
class _Hm2AgentGlobalPortSecurityMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentGlobalPortSecurityMode_Type.__name__=_G
_Hm2AgentGlobalPortSecurityMode_Object=MibScalar
hm2AgentGlobalPortSecurityMode=_Hm2AgentGlobalPortSecurityMode_Object((1,3,6,1,4,1,248,12,20,1,1),_Hm2AgentGlobalPortSecurityMode_Type())
hm2AgentGlobalPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentGlobalPortSecurityMode.setStatus(_A)
_Hm2AgentPortSecurityTable_Object=MibTable
hm2AgentPortSecurityTable=_Hm2AgentPortSecurityTable_Object((1,3,6,1,4,1,248,12,20,1,2))
if mibBuilder.loadTexts:hm2AgentPortSecurityTable.setStatus(_A)
_Hm2AgentPortSecurityEntry_Object=MibTableRow
hm2AgentPortSecurityEntry=_Hm2AgentPortSecurityEntry_Object((1,3,6,1,4,1,248,12,20,1,2,1))
hm2AgentPortSecurityEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hm2AgentPortSecurityEntry.setStatus(_A)
class _Hm2AgentPortSecurityMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentPortSecurityMode_Type.__name__=_G
_Hm2AgentPortSecurityMode_Object=MibTableColumn
hm2AgentPortSecurityMode=_Hm2AgentPortSecurityMode_Object((1,3,6,1,4,1,248,12,20,1,2,1,1),_Hm2AgentPortSecurityMode_Type())
hm2AgentPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityMode.setStatus(_A)
class _Hm2AgentPortSecurityDynamicLimit_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_Hm2AgentPortSecurityDynamicLimit_Type.__name__=_H
_Hm2AgentPortSecurityDynamicLimit_Object=MibTableColumn
hm2AgentPortSecurityDynamicLimit=_Hm2AgentPortSecurityDynamicLimit_Object((1,3,6,1,4,1,248,12,20,1,2,1,2),_Hm2AgentPortSecurityDynamicLimit_Type())
hm2AgentPortSecurityDynamicLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityDynamicLimit.setStatus(_A)
class _Hm2AgentPortSecurityStaticLimit_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Hm2AgentPortSecurityStaticLimit_Type.__name__=_H
_Hm2AgentPortSecurityStaticLimit_Object=MibTableColumn
hm2AgentPortSecurityStaticLimit=_Hm2AgentPortSecurityStaticLimit_Object((1,3,6,1,4,1,248,12,20,1,2,1,3),_Hm2AgentPortSecurityStaticLimit_Type())
hm2AgentPortSecurityStaticLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticLimit.setStatus(_A)
class _Hm2AgentPortSecurityViolationTrapMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentPortSecurityViolationTrapMode_Type.__name__=_G
_Hm2AgentPortSecurityViolationTrapMode_Object=MibTableColumn
hm2AgentPortSecurityViolationTrapMode=_Hm2AgentPortSecurityViolationTrapMode_Object((1,3,6,1,4,1,248,12,20,1,2,1,4),_Hm2AgentPortSecurityViolationTrapMode_Type())
hm2AgentPortSecurityViolationTrapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityViolationTrapMode.setStatus(_A)
class _Hm2AgentPortSecurityStaticMACs_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1536))
_Hm2AgentPortSecurityStaticMACs_Type.__name__=_I
_Hm2AgentPortSecurityStaticMACs_Object=MibTableColumn
hm2AgentPortSecurityStaticMACs=_Hm2AgentPortSecurityStaticMACs_Object((1,3,6,1,4,1,248,12,20,1,2,1,6),_Hm2AgentPortSecurityStaticMACs_Type())
hm2AgentPortSecurityStaticMACs.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticMACs.setStatus(_A)
_Hm2AgentPortSecurityLastDiscardedMAC_Type=DisplayString
_Hm2AgentPortSecurityLastDiscardedMAC_Object=MibTableColumn
hm2AgentPortSecurityLastDiscardedMAC=_Hm2AgentPortSecurityLastDiscardedMAC_Object((1,3,6,1,4,1,248,12,20,1,2,1,7),_Hm2AgentPortSecurityLastDiscardedMAC_Type())
hm2AgentPortSecurityLastDiscardedMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityLastDiscardedMAC.setStatus(_A)
_Hm2AgentPortSecurityMACAddressAdd_Type=DisplayString
_Hm2AgentPortSecurityMACAddressAdd_Object=MibTableColumn
hm2AgentPortSecurityMACAddressAdd=_Hm2AgentPortSecurityMACAddressAdd_Object((1,3,6,1,4,1,248,12,20,1,2,1,8),_Hm2AgentPortSecurityMACAddressAdd_Type())
hm2AgentPortSecurityMACAddressAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityMACAddressAdd.setStatus(_A)
_Hm2AgentPortSecurityMACAddressRemove_Type=DisplayString
_Hm2AgentPortSecurityMACAddressRemove_Object=MibTableColumn
hm2AgentPortSecurityMACAddressRemove=_Hm2AgentPortSecurityMACAddressRemove_Object((1,3,6,1,4,1,248,12,20,1,2,1,9),_Hm2AgentPortSecurityMACAddressRemove_Type())
hm2AgentPortSecurityMACAddressRemove.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityMACAddressRemove.setStatus(_A)
_Hm2AgentPortSecurityMACAddressMove_Type=HmEnabledStatus
_Hm2AgentPortSecurityMACAddressMove_Object=MibTableColumn
hm2AgentPortSecurityMACAddressMove=_Hm2AgentPortSecurityMACAddressMove_Object((1,3,6,1,4,1,248,12,20,1,2,1,10),_Hm2AgentPortSecurityMACAddressMove_Type())
hm2AgentPortSecurityMACAddressMove.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityMACAddressMove.setStatus(_A)
_Hm2AgentPortSecurityDynamicCount_Type=Unsigned32
_Hm2AgentPortSecurityDynamicCount_Object=MibTableColumn
hm2AgentPortSecurityDynamicCount=_Hm2AgentPortSecurityDynamicCount_Object((1,3,6,1,4,1,248,12,20,1,2,1,20),_Hm2AgentPortSecurityDynamicCount_Type())
hm2AgentPortSecurityDynamicCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityDynamicCount.setStatus(_A)
_Hm2AgentPortSecurityStaticCount_Type=Unsigned32
_Hm2AgentPortSecurityStaticCount_Object=MibTableColumn
hm2AgentPortSecurityStaticCount=_Hm2AgentPortSecurityStaticCount_Object((1,3,6,1,4,1,248,12,20,1,2,1,21),_Hm2AgentPortSecurityStaticCount_Type())
hm2AgentPortSecurityStaticCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticCount.setStatus(_A)
_Hm2AgentPortSecurityViolationTrapCount_Type=Unsigned32
_Hm2AgentPortSecurityViolationTrapCount_Object=MibTableColumn
hm2AgentPortSecurityViolationTrapCount=_Hm2AgentPortSecurityViolationTrapCount_Object((1,3,6,1,4,1,248,12,20,1,2,1,22),_Hm2AgentPortSecurityViolationTrapCount_Type())
hm2AgentPortSecurityViolationTrapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityViolationTrapCount.setStatus(_A)
class _Hm2AgentPortSecurityViolationTrapFrequency_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_Hm2AgentPortSecurityViolationTrapFrequency_Type.__name__=_H
_Hm2AgentPortSecurityViolationTrapFrequency_Object=MibTableColumn
hm2AgentPortSecurityViolationTrapFrequency=_Hm2AgentPortSecurityViolationTrapFrequency_Object((1,3,6,1,4,1,248,12,20,1,2,1,23),_Hm2AgentPortSecurityViolationTrapFrequency_Type())
hm2AgentPortSecurityViolationTrapFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityViolationTrapFrequency.setStatus(_A)
class _Hm2AgentPortSecurityAutoDisable_Type(TruthValue):defaultValue=1
_Hm2AgentPortSecurityAutoDisable_Type.__name__=_K
_Hm2AgentPortSecurityAutoDisable_Object=MibTableColumn
hm2AgentPortSecurityAutoDisable=_Hm2AgentPortSecurityAutoDisable_Object((1,3,6,1,4,1,248,12,20,1,2,1,248),_Hm2AgentPortSecurityAutoDisable_Type())
hm2AgentPortSecurityAutoDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityAutoDisable.setStatus(_A)
_Hm2AgentPortSecurityStaticIpCount_Type=Unsigned32
_Hm2AgentPortSecurityStaticIpCount_Object=MibTableColumn
hm2AgentPortSecurityStaticIpCount=_Hm2AgentPortSecurityStaticIpCount_Object((1,3,6,1,4,1,248,12,20,1,2,1,249),_Hm2AgentPortSecurityStaticIpCount_Type())
hm2AgentPortSecurityStaticIpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticIpCount.setStatus(_A)
class _Hm2AgentPortSecurityStaticIPs_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1536))
_Hm2AgentPortSecurityStaticIPs_Type.__name__=_I
_Hm2AgentPortSecurityStaticIPs_Object=MibTableColumn
hm2AgentPortSecurityStaticIPs=_Hm2AgentPortSecurityStaticIPs_Object((1,3,6,1,4,1,248,12,20,1,2,1,250),_Hm2AgentPortSecurityStaticIPs_Type())
hm2AgentPortSecurityStaticIPs.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticIPs.setStatus(_A)
_Hm2AgentPortSecurityIPAddressAdd_Type=DisplayString
_Hm2AgentPortSecurityIPAddressAdd_Object=MibTableColumn
hm2AgentPortSecurityIPAddressAdd=_Hm2AgentPortSecurityIPAddressAdd_Object((1,3,6,1,4,1,248,12,20,1,2,1,251),_Hm2AgentPortSecurityIPAddressAdd_Type())
hm2AgentPortSecurityIPAddressAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityIPAddressAdd.setStatus(_A)
_Hm2AgentPortSecurityIPAddressRemove_Type=DisplayString
_Hm2AgentPortSecurityIPAddressRemove_Object=MibTableColumn
hm2AgentPortSecurityIPAddressRemove=_Hm2AgentPortSecurityIPAddressRemove_Object((1,3,6,1,4,1,248,12,20,1,2,1,252),_Hm2AgentPortSecurityIPAddressRemove_Type())
hm2AgentPortSecurityIPAddressRemove.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityIPAddressRemove.setStatus(_A)
_Hm2AgentPortSecurityDynamicTable_Object=MibTable
hm2AgentPortSecurityDynamicTable=_Hm2AgentPortSecurityDynamicTable_Object((1,3,6,1,4,1,248,12,20,1,3))
if mibBuilder.loadTexts:hm2AgentPortSecurityDynamicTable.setStatus(_A)
_Hm2AgentPortSecurityDynamicEntry_Object=MibTableRow
hm2AgentPortSecurityDynamicEntry=_Hm2AgentPortSecurityDynamicEntry_Object((1,3,6,1,4,1,248,12,20,1,3,1))
hm2AgentPortSecurityDynamicEntry.setIndexNames((0,_E,_F),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:hm2AgentPortSecurityDynamicEntry.setStatus(_A)
_Hm2AgentPortSecurityDynamicVLANId_Type=Unsigned32
_Hm2AgentPortSecurityDynamicVLANId_Object=MibTableColumn
hm2AgentPortSecurityDynamicVLANId=_Hm2AgentPortSecurityDynamicVLANId_Object((1,3,6,1,4,1,248,12,20,1,3,1,1),_Hm2AgentPortSecurityDynamicVLANId_Type())
hm2AgentPortSecurityDynamicVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityDynamicVLANId.setStatus(_A)
_Hm2AgentPortSecurityDynamicMACAddress_Type=MacAddress
_Hm2AgentPortSecurityDynamicMACAddress_Object=MibTableColumn
hm2AgentPortSecurityDynamicMACAddress=_Hm2AgentPortSecurityDynamicMACAddress_Object((1,3,6,1,4,1,248,12,20,1,3,1,2),_Hm2AgentPortSecurityDynamicMACAddress_Type())
hm2AgentPortSecurityDynamicMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityDynamicMACAddress.setStatus(_A)
_Hm2AgentPortSecurityStaticTable_Object=MibTable
hm2AgentPortSecurityStaticTable=_Hm2AgentPortSecurityStaticTable_Object((1,3,6,1,4,1,248,12,20,1,10))
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticTable.setStatus(_A)
_Hm2AgentPortSecurityStaticEntry_Object=MibTableRow
hm2AgentPortSecurityStaticEntry=_Hm2AgentPortSecurityStaticEntry_Object((1,3,6,1,4,1,248,12,20,1,10,1))
hm2AgentPortSecurityStaticEntry.setIndexNames((0,_E,_F),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticEntry.setStatus(_A)
_Hm2AgentPortSecurityStaticVLANId_Type=Unsigned32
_Hm2AgentPortSecurityStaticVLANId_Object=MibTableColumn
hm2AgentPortSecurityStaticVLANId=_Hm2AgentPortSecurityStaticVLANId_Object((1,3,6,1,4,1,248,12,20,1,10,1,1),_Hm2AgentPortSecurityStaticVLANId_Type())
hm2AgentPortSecurityStaticVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticVLANId.setStatus(_A)
_Hm2AgentPortSecurityStaticMACAddress_Type=MacAddress
_Hm2AgentPortSecurityStaticMACAddress_Object=MibTableColumn
hm2AgentPortSecurityStaticMACAddress=_Hm2AgentPortSecurityStaticMACAddress_Object((1,3,6,1,4,1,248,12,20,1,10,1,2),_Hm2AgentPortSecurityStaticMACAddress_Type())
hm2AgentPortSecurityStaticMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticMACAddress.setStatus(_A)
_Hm2AgentPortSecurityIpStaticTable_Object=MibTable
hm2AgentPortSecurityIpStaticTable=_Hm2AgentPortSecurityIpStaticTable_Object((1,3,6,1,4,1,248,12,20,1,11))
if mibBuilder.loadTexts:hm2AgentPortSecurityIpStaticTable.setStatus(_A)
_Hm2AgentPortSecurityIpStaticEntry_Object=MibTableRow
hm2AgentPortSecurityIpStaticEntry=_Hm2AgentPortSecurityIpStaticEntry_Object((1,3,6,1,4,1,248,12,20,1,11,1))
hm2AgentPortSecurityIpStaticEntry.setIndexNames((0,_E,_F),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:hm2AgentPortSecurityIpStaticEntry.setStatus(_A)
_Hm2AgentPortSecurityStaticIpVLANId_Type=Unsigned32
_Hm2AgentPortSecurityStaticIpVLANId_Object=MibTableColumn
hm2AgentPortSecurityStaticIpVLANId=_Hm2AgentPortSecurityStaticIpVLANId_Object((1,3,6,1,4,1,248,12,20,1,11,1,1),_Hm2AgentPortSecurityStaticIpVLANId_Type())
hm2AgentPortSecurityStaticIpVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticIpVLANId.setStatus(_A)
_Hm2AgentPortSecurityStaticIpAddress_Type=IpAddress
_Hm2AgentPortSecurityStaticIpAddress_Object=MibTableColumn
hm2AgentPortSecurityStaticIpAddress=_Hm2AgentPortSecurityStaticIpAddress_Object((1,3,6,1,4,1,248,12,20,1,11,1,2),_Hm2AgentPortSecurityStaticIpAddress_Type())
hm2AgentPortSecurityStaticIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentPortSecurityStaticIpAddress.setStatus(_A)
class _Hm2AgentPortSecurityOperationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('macAddressBased',1),('ipAddressBased',2)))
_Hm2AgentPortSecurityOperationMode_Type.__name__=_J
_Hm2AgentPortSecurityOperationMode_Object=MibScalar
hm2AgentPortSecurityOperationMode=_Hm2AgentPortSecurityOperationMode_Object((1,3,6,1,4,1,248,12,20,1,12),_Hm2AgentPortSecurityOperationMode_Type())
hm2AgentPortSecurityOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentPortSecurityOperationMode.setStatus(_A)
_Hm2AgentPortSecurityTraps_ObjectIdentity=ObjectIdentity
hm2AgentPortSecurityTraps=_Hm2AgentPortSecurityTraps_ObjectIdentity((1,3,6,1,4,1,248,12,20,2))
hm2AgentPortSecurityViolation=NotificationType((1,3,6,1,4,1,248,12,20,2,1))
hm2AgentPortSecurityViolation.setObjects(*((_E,_F),(_D,_R)))
if mibBuilder.loadTexts:hm2AgentPortSecurityViolation.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hm2PlatformPortSecurity':hm2PlatformPortSecurity,'hm2AgentPortSecurityGroup':hm2AgentPortSecurityGroup,'hm2AgentGlobalPortSecurityMode':hm2AgentGlobalPortSecurityMode,'hm2AgentPortSecurityTable':hm2AgentPortSecurityTable,'hm2AgentPortSecurityEntry':hm2AgentPortSecurityEntry,'hm2AgentPortSecurityMode':hm2AgentPortSecurityMode,'hm2AgentPortSecurityDynamicLimit':hm2AgentPortSecurityDynamicLimit,'hm2AgentPortSecurityStaticLimit':hm2AgentPortSecurityStaticLimit,'hm2AgentPortSecurityViolationTrapMode':hm2AgentPortSecurityViolationTrapMode,'hm2AgentPortSecurityStaticMACs':hm2AgentPortSecurityStaticMACs,_R:hm2AgentPortSecurityLastDiscardedMAC,'hm2AgentPortSecurityMACAddressAdd':hm2AgentPortSecurityMACAddressAdd,'hm2AgentPortSecurityMACAddressRemove':hm2AgentPortSecurityMACAddressRemove,'hm2AgentPortSecurityMACAddressMove':hm2AgentPortSecurityMACAddressMove,'hm2AgentPortSecurityDynamicCount':hm2AgentPortSecurityDynamicCount,'hm2AgentPortSecurityStaticCount':hm2AgentPortSecurityStaticCount,'hm2AgentPortSecurityViolationTrapCount':hm2AgentPortSecurityViolationTrapCount,'hm2AgentPortSecurityViolationTrapFrequency':hm2AgentPortSecurityViolationTrapFrequency,'hm2AgentPortSecurityAutoDisable':hm2AgentPortSecurityAutoDisable,'hm2AgentPortSecurityStaticIpCount':hm2AgentPortSecurityStaticIpCount,'hm2AgentPortSecurityStaticIPs':hm2AgentPortSecurityStaticIPs,'hm2AgentPortSecurityIPAddressAdd':hm2AgentPortSecurityIPAddressAdd,'hm2AgentPortSecurityIPAddressRemove':hm2AgentPortSecurityIPAddressRemove,'hm2AgentPortSecurityDynamicTable':hm2AgentPortSecurityDynamicTable,'hm2AgentPortSecurityDynamicEntry':hm2AgentPortSecurityDynamicEntry,_L:hm2AgentPortSecurityDynamicVLANId,_M:hm2AgentPortSecurityDynamicMACAddress,'hm2AgentPortSecurityStaticTable':hm2AgentPortSecurityStaticTable,'hm2AgentPortSecurityStaticEntry':hm2AgentPortSecurityStaticEntry,_N:hm2AgentPortSecurityStaticVLANId,_O:hm2AgentPortSecurityStaticMACAddress,'hm2AgentPortSecurityIpStaticTable':hm2AgentPortSecurityIpStaticTable,'hm2AgentPortSecurityIpStaticEntry':hm2AgentPortSecurityIpStaticEntry,_P:hm2AgentPortSecurityStaticIpVLANId,_Q:hm2AgentPortSecurityStaticIpAddress,'hm2AgentPortSecurityOperationMode':hm2AgentPortSecurityOperationMode,'hm2AgentPortSecurityTraps':hm2AgentPortSecurityTraps,'hm2AgentPortSecurityViolation':hm2AgentPortSecurityViolation})