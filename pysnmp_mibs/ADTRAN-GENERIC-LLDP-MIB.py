_O='interfaceName'
_N='networkAddress'
_M='macAddress'
_L='portComponent'
_K='interfaceAlias'
_J='Integer32'
_I='sysName'
_H='SNMPv2-MIB'
_G='adTrapInformSeqNum'
_F='ADTRAN-GENTRAPINFORM-MIB'
_E='SnmpAdminString'
_D='IF-MIB'
_C='ifIndex'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adTrapInformSeqNum,=mibBuilder.importSymbols(_F,_G)
adGenLldp,adGenLldpID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenLldp','adGenLldpID')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_C)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
adGenLldpMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,46,1))
if mibBuilder.loadTexts:adGenLldpMIB.setRevisions(('2013-09-18 00:00','2011-10-18 00:00'))
class AdGenChassisIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('chassisComponent',1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),('local',7)))
class AdGenChassisId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class AdGenPortIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),('agentCircuitId',6),('local',7)))
class AdGenPortId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class AdGenManAddrIfSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),(_C,2),('systemPortNumber',3)))
class AdGenManAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class AdGenSystemCapabilitiesMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('other',0),('repeater',1),('bridge',2),('wlanAccessPoint',3),('router',4),('telephone',5),('docsisCableDevice',6),('stationOnly',7)))
_AdGenLldpConfiguration_ObjectIdentity=ObjectIdentity
adGenLldpConfiguration=_AdGenLldpConfiguration_ObjectIdentity((1,3,6,1,4,1,664,5,70,46,1))
_AdGenLldpProvTable_Object=MibTable
adGenLldpProvTable=_AdGenLldpProvTable_Object((1,3,6,1,4,1,664,5,70,46,1,1))
if mibBuilder.loadTexts:adGenLldpProvTable.setStatus(_A)
_AdGenLldpProvEntry_Object=MibTableRow
adGenLldpProvEntry=_AdGenLldpProvEntry_Object((1,3,6,1,4,1,664,5,70,46,1,1,1))
adGenLldpProvEntry.setIndexNames((0,_D,_C))
if mibBuilder.loadTexts:adGenLldpProvEntry.setStatus(_A)
class _AdGenLldpConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('txOnly',1),('rxOnly',2),('txAndRx',3),('disabled',4)))
_AdGenLldpConfigState_Type.__name__=_J
_AdGenLldpConfigState_Object=MibTableColumn
adGenLldpConfigState=_AdGenLldpConfigState_Object((1,3,6,1,4,1,664,5,70,46,1,1,1,1),_AdGenLldpConfigState_Type())
adGenLldpConfigState.setMaxAccess('read-write')
if mibBuilder.loadTexts:adGenLldpConfigState.setStatus(_A)
_AdGenLldpStatistics_ObjectIdentity=ObjectIdentity
adGenLldpStatistics=_AdGenLldpStatistics_ObjectIdentity((1,3,6,1,4,1,664,5,70,46,2))
_AdGenLldpLocalSystemData_ObjectIdentity=ObjectIdentity
adGenLldpLocalSystemData=_AdGenLldpLocalSystemData_ObjectIdentity((1,3,6,1,4,1,664,5,70,46,3))
_AdGenLldpRemoteSystemData_ObjectIdentity=ObjectIdentity
adGenLldpRemoteSystemData=_AdGenLldpRemoteSystemData_ObjectIdentity((1,3,6,1,4,1,664,5,70,46,4))
_AdGenLldpRemSysDataTable_Object=MibTable
adGenLldpRemSysDataTable=_AdGenLldpRemSysDataTable_Object((1,3,6,1,4,1,664,5,70,46,4,1))
if mibBuilder.loadTexts:adGenLldpRemSysDataTable.setStatus(_A)
_AdGenLldpRemSysDataEntry_Object=MibTableRow
adGenLldpRemSysDataEntry=_AdGenLldpRemSysDataEntry_Object((1,3,6,1,4,1,664,5,70,46,4,1,1))
adGenLldpRemSysDataEntry.setIndexNames((0,_D,_C))
if mibBuilder.loadTexts:adGenLldpRemSysDataEntry.setStatus(_A)
_AdGenLldpRemChassisIdSubtype_Type=AdGenChassisIdSubtype
_AdGenLldpRemChassisIdSubtype_Object=MibTableColumn
adGenLldpRemChassisIdSubtype=_AdGenLldpRemChassisIdSubtype_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,1),_AdGenLldpRemChassisIdSubtype_Type())
adGenLldpRemChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemChassisIdSubtype.setStatus(_A)
_AdGenLldpRemChassisId_Type=AdGenChassisId
_AdGenLldpRemChassisId_Object=MibTableColumn
adGenLldpRemChassisId=_AdGenLldpRemChassisId_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,2),_AdGenLldpRemChassisId_Type())
adGenLldpRemChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemChassisId.setStatus(_A)
_AdGenLldpRemPortIdSubtype_Type=AdGenPortIdSubtype
_AdGenLldpRemPortIdSubtype_Object=MibTableColumn
adGenLldpRemPortIdSubtype=_AdGenLldpRemPortIdSubtype_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,3),_AdGenLldpRemPortIdSubtype_Type())
adGenLldpRemPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemPortIdSubtype.setStatus(_A)
_AdGenLldpRemPortId_Type=AdGenPortId
_AdGenLldpRemPortId_Object=MibTableColumn
adGenLldpRemPortId=_AdGenLldpRemPortId_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,4),_AdGenLldpRemPortId_Type())
adGenLldpRemPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemPortId.setStatus(_A)
class _AdGenLldpRemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AdGenLldpRemPortDesc_Type.__name__=_E
_AdGenLldpRemPortDesc_Object=MibTableColumn
adGenLldpRemPortDesc=_AdGenLldpRemPortDesc_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,5),_AdGenLldpRemPortDesc_Type())
adGenLldpRemPortDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemPortDesc.setStatus(_A)
class _AdGenLldpRemSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AdGenLldpRemSysName_Type.__name__=_E
_AdGenLldpRemSysName_Object=MibTableColumn
adGenLldpRemSysName=_AdGenLldpRemSysName_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,6),_AdGenLldpRemSysName_Type())
adGenLldpRemSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemSysName.setStatus(_A)
class _AdGenLldpRemSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AdGenLldpRemSysDesc_Type.__name__=_E
_AdGenLldpRemSysDesc_Object=MibTableColumn
adGenLldpRemSysDesc=_AdGenLldpRemSysDesc_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,7),_AdGenLldpRemSysDesc_Type())
adGenLldpRemSysDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemSysDesc.setStatus(_A)
_AdGenLldpRemSysCapSupported_Type=AdGenSystemCapabilitiesMap
_AdGenLldpRemSysCapSupported_Object=MibTableColumn
adGenLldpRemSysCapSupported=_AdGenLldpRemSysCapSupported_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,8),_AdGenLldpRemSysCapSupported_Type())
adGenLldpRemSysCapSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemSysCapSupported.setStatus(_A)
_AdGenLldpRemSysCapEnabled_Type=AdGenSystemCapabilitiesMap
_AdGenLldpRemSysCapEnabled_Object=MibTableColumn
adGenLldpRemSysCapEnabled=_AdGenLldpRemSysCapEnabled_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,9),_AdGenLldpRemSysCapEnabled_Type())
adGenLldpRemSysCapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemSysCapEnabled.setStatus(_A)
_AdGenLldpRemManAddrSubtype_Type=AddressFamilyNumbers
_AdGenLldpRemManAddrSubtype_Object=MibTableColumn
adGenLldpRemManAddrSubtype=_AdGenLldpRemManAddrSubtype_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,10),_AdGenLldpRemManAddrSubtype_Type())
adGenLldpRemManAddrSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemManAddrSubtype.setStatus(_A)
_AdGenLldpRemManAddr_Type=AdGenManAddress
_AdGenLldpRemManAddr_Object=MibTableColumn
adGenLldpRemManAddr=_AdGenLldpRemManAddr_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,11),_AdGenLldpRemManAddr_Type())
adGenLldpRemManAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemManAddr.setStatus(_A)
_AdGenLldpRemManAddrIfSubtype_Type=AdGenManAddrIfSubtype
_AdGenLldpRemManAddrIfSubtype_Object=MibTableColumn
adGenLldpRemManAddrIfSubtype=_AdGenLldpRemManAddrIfSubtype_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,12),_AdGenLldpRemManAddrIfSubtype_Type())
adGenLldpRemManAddrIfSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemManAddrIfSubtype.setStatus(_A)
_AdGenLldpRemManAddrIfId_Type=Integer32
_AdGenLldpRemManAddrIfId_Object=MibTableColumn
adGenLldpRemManAddrIfId=_AdGenLldpRemManAddrIfId_Object((1,3,6,1,4,1,664,5,70,46,4,1,1,13),_AdGenLldpRemManAddrIfId_Type())
adGenLldpRemManAddrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenLldpRemManAddrIfId.setStatus(_A)
_AdGenLldpExtentsions_ObjectIdentity=ObjectIdentity
adGenLldpExtentsions=_AdGenLldpExtentsions_ObjectIdentity((1,3,6,1,4,1,664,5,70,46,5))
_AdGenLldpEvents_ObjectIdentity=ObjectIdentity
adGenLldpEvents=_AdGenLldpEvents_ObjectIdentity((1,3,6,1,4,1,664,5,70,46,6))
_AdGenLldpTraps_ObjectIdentity=ObjectIdentity
adGenLldpTraps=_AdGenLldpTraps_ObjectIdentity((1,3,6,1,4,1,664,5,70,46,6,0))
adGenLldpPeerRemoved=NotificationType((1,3,6,1,4,1,664,5,70,46,6,0,1))
adGenLldpPeerRemoved.setObjects(*((_F,_G),(_H,_I),(_D,_C)))
if mibBuilder.loadTexts:adGenLldpPeerRemoved.setStatus(_A)
adGenLldpPeerAdded=NotificationType((1,3,6,1,4,1,664,5,70,46,6,0,2))
adGenLldpPeerAdded.setObjects(*((_F,_G),(_H,_I),(_D,_C)))
if mibBuilder.loadTexts:adGenLldpPeerAdded.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENERIC-LLDP-MIB',**{'AdGenChassisIdSubtype':AdGenChassisIdSubtype,'AdGenChassisId':AdGenChassisId,'AdGenPortIdSubtype':AdGenPortIdSubtype,'AdGenPortId':AdGenPortId,'AdGenManAddrIfSubtype':AdGenManAddrIfSubtype,'AdGenManAddress':AdGenManAddress,'AdGenSystemCapabilitiesMap':AdGenSystemCapabilitiesMap,'adGenLldpConfiguration':adGenLldpConfiguration,'adGenLldpProvTable':adGenLldpProvTable,'adGenLldpProvEntry':adGenLldpProvEntry,'adGenLldpConfigState':adGenLldpConfigState,'adGenLldpStatistics':adGenLldpStatistics,'adGenLldpLocalSystemData':adGenLldpLocalSystemData,'adGenLldpRemoteSystemData':adGenLldpRemoteSystemData,'adGenLldpRemSysDataTable':adGenLldpRemSysDataTable,'adGenLldpRemSysDataEntry':adGenLldpRemSysDataEntry,'adGenLldpRemChassisIdSubtype':adGenLldpRemChassisIdSubtype,'adGenLldpRemChassisId':adGenLldpRemChassisId,'adGenLldpRemPortIdSubtype':adGenLldpRemPortIdSubtype,'adGenLldpRemPortId':adGenLldpRemPortId,'adGenLldpRemPortDesc':adGenLldpRemPortDesc,'adGenLldpRemSysName':adGenLldpRemSysName,'adGenLldpRemSysDesc':adGenLldpRemSysDesc,'adGenLldpRemSysCapSupported':adGenLldpRemSysCapSupported,'adGenLldpRemSysCapEnabled':adGenLldpRemSysCapEnabled,'adGenLldpRemManAddrSubtype':adGenLldpRemManAddrSubtype,'adGenLldpRemManAddr':adGenLldpRemManAddr,'adGenLldpRemManAddrIfSubtype':adGenLldpRemManAddrIfSubtype,'adGenLldpRemManAddrIfId':adGenLldpRemManAddrIfId,'adGenLldpExtentsions':adGenLldpExtentsions,'adGenLldpEvents':adGenLldpEvents,'adGenLldpTraps':adGenLldpTraps,'adGenLldpPeerRemoved':adGenLldpPeerRemoved,'adGenLldpPeerAdded':adGenLldpPeerAdded,'adGenLldpMIB':adGenLldpMIB})