_K='ciscoFcDaConfigGroup'
_J='cfdaConfigRowStatus'
_I='cfdaConfigDeviceId'
_H='cfdaConfigDeviceType'
_G='cfdaConfigDeviceAlias'
_F='SnmpAdminString'
_E='CdpvmDevType'
_D='OctetString'
_C='read-create'
_B='CISCO-FC-DEVICE-ALIAS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CdpvmDevType,=mibBuilder.importSymbols('CISCO-DYNAMIC-PORT-VSAN-MIB',_E)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoFcDeviceAliasMIB=ModuleIdentity((1,3,6,1,4,1,9,9,430))
if mibBuilder.loadTexts:ciscoFcDeviceAliasMIB.setRevisions(('2004-09-20 00:00',))
_CfdaMIBNotifs_ObjectIdentity=ObjectIdentity
cfdaMIBNotifs=_CfdaMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,430,0))
_CfdaMIBObjects_ObjectIdentity=ObjectIdentity
cfdaMIBObjects=_CfdaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,430,1))
_CfdaConfiguration_ObjectIdentity=ObjectIdentity
cfdaConfiguration=_CfdaConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,430,1,1))
_CfdaConfigTable_Object=MibTable
cfdaConfigTable=_CfdaConfigTable_Object((1,3,6,1,4,1,9,9,430,1,1,1))
if mibBuilder.loadTexts:cfdaConfigTable.setStatus(_A)
_CfdaConfigEntry_Object=MibTableRow
cfdaConfigEntry=_CfdaConfigEntry_Object((1,3,6,1,4,1,9,9,430,1,1,1,1))
cfdaConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cfdaConfigEntry.setStatus(_A)
class _CfdaConfigDeviceAlias_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CfdaConfigDeviceAlias_Type.__name__=_F
_CfdaConfigDeviceAlias_Object=MibTableColumn
cfdaConfigDeviceAlias=_CfdaConfigDeviceAlias_Object((1,3,6,1,4,1,9,9,430,1,1,1,1,1),_CfdaConfigDeviceAlias_Type())
cfdaConfigDeviceAlias.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfdaConfigDeviceAlias.setStatus(_A)
class _CfdaConfigDeviceType_Type(CdpvmDevType):defaultValue=1
_CfdaConfigDeviceType_Type.__name__=_E
_CfdaConfigDeviceType_Object=MibTableColumn
cfdaConfigDeviceType=_CfdaConfigDeviceType_Object((1,3,6,1,4,1,9,9,430,1,1,1,1,2),_CfdaConfigDeviceType_Type())
cfdaConfigDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdaConfigDeviceType.setStatus(_A)
class _CfdaConfigDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CfdaConfigDeviceId_Type.__name__=_D
_CfdaConfigDeviceId_Object=MibTableColumn
cfdaConfigDeviceId=_CfdaConfigDeviceId_Object((1,3,6,1,4,1,9,9,430,1,1,1,1,3),_CfdaConfigDeviceId_Type())
cfdaConfigDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdaConfigDeviceId.setStatus(_A)
_CfdaConfigRowStatus_Type=RowStatus
_CfdaConfigRowStatus_Object=MibTableColumn
cfdaConfigRowStatus=_CfdaConfigRowStatus_Object((1,3,6,1,4,1,9,9,430,1,1,1,1,4),_CfdaConfigRowStatus_Type())
cfdaConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdaConfigRowStatus.setStatus(_A)
_CfdaMIBConform_ObjectIdentity=ObjectIdentity
cfdaMIBConform=_CfdaMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,430,2))
_CiscoFcDaMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFcDaMIBCompliances=_CiscoFcDaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,430,2,1))
_CiscoFcDaMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFcDaMIBGroups=_CiscoFcDaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,430,2,2))
ciscoFcDaConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,430,2,2,1))
ciscoFcDaConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ciscoFcDaConfigGroup.setStatus(_A)
ciscoFcDaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,430,2,1,1))
ciscoFcDaMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoFcDaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFcDeviceAliasMIB':ciscoFcDeviceAliasMIB,'cfdaMIBNotifs':cfdaMIBNotifs,'cfdaMIBObjects':cfdaMIBObjects,'cfdaConfiguration':cfdaConfiguration,'cfdaConfigTable':cfdaConfigTable,'cfdaConfigEntry':cfdaConfigEntry,_G:cfdaConfigDeviceAlias,_H:cfdaConfigDeviceType,_I:cfdaConfigDeviceId,_J:cfdaConfigRowStatus,'cfdaMIBConform':cfdaMIBConform,'ciscoFcDaMIBCompliances':ciscoFcDaMIBCompliances,'ciscoFcDaMIBCompliance':ciscoFcDaMIBCompliance,'ciscoFcDaMIBGroups':ciscoFcDaMIBGroups,_K:ciscoFcDaConfigGroup})