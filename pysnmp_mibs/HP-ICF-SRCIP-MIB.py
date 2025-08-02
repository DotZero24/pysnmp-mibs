_K='hpicfSrcIpBaseGroup'
_J='hpicfSrcIpAddress'
_I='hpicfSrcIpAddrIfIndex'
_H='hpicfSrcIpAddrPolicy'
_G='not-accessible'
_F='hpicfSrcIpProtocolIndex'
_E='hpicfSrcIpAddressType'
_D='read-write'
_C='Integer32'
_B='HP-ICF-SRCIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpicfCommon,=mibBuilder.importSymbols('HP-ICF-OID','hpicfCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfSrcIpMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,1,13))
if mibBuilder.loadTexts:hpicfSrcIpMIB.setRevisions(('2020-06-20 00:00','2016-08-29 00:00','2011-07-21 00:00','2009-04-30 00:00','2008-10-10 00:00'))
_HpicfSrcIpConfig_ObjectIdentity=ObjectIdentity
hpicfSrcIpConfig=_HpicfSrcIpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,13,1))
_HpicfSrcIpAddrPolicyTable_Object=MibTable
hpicfSrcIpAddrPolicyTable=_HpicfSrcIpAddrPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,1,13,1,1))
if mibBuilder.loadTexts:hpicfSrcIpAddrPolicyTable.setStatus(_A)
_HpicfSrcIpAddrPolicyEntry_Object=MibTableRow
hpicfSrcIpAddrPolicyEntry=_HpicfSrcIpAddrPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,1,13,1,1,1))
hpicfSrcIpAddrPolicyEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:hpicfSrcIpAddrPolicyEntry.setStatus(_A)
_HpicfSrcIpAddressType_Type=InetAddressType
_HpicfSrcIpAddressType_Object=MibTableColumn
hpicfSrcIpAddressType=_HpicfSrcIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,1,13,1,1,1,1),_HpicfSrcIpAddressType_Type())
hpicfSrcIpAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfSrcIpAddressType.setStatus(_A)
class _HpicfSrcIpProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('tacacs',1),('radius',2),('syslog',3),('telnet',4),('tftp',5),('sntp',6),('sflow',7),('tunnelednodeserver',8),('radsec',9),('central',10)))
_HpicfSrcIpProtocolIndex_Type.__name__=_C
_HpicfSrcIpProtocolIndex_Object=MibTableColumn
hpicfSrcIpProtocolIndex=_HpicfSrcIpProtocolIndex_Object((1,3,6,1,4,1,11,2,14,11,1,13,1,1,1,2),_HpicfSrcIpProtocolIndex_Type())
hpicfSrcIpProtocolIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfSrcIpProtocolIndex.setStatus(_A)
class _HpicfSrcIpAddrPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('outgoingInterface',1),('configuredIpAddr',2),('configuredInterface',3)))
_HpicfSrcIpAddrPolicy_Type.__name__=_C
_HpicfSrcIpAddrPolicy_Object=MibTableColumn
hpicfSrcIpAddrPolicy=_HpicfSrcIpAddrPolicy_Object((1,3,6,1,4,1,11,2,14,11,1,13,1,1,1,3),_HpicfSrcIpAddrPolicy_Type())
hpicfSrcIpAddrPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSrcIpAddrPolicy.setStatus(_A)
_HpicfSrcIpAddrIfIndex_Type=InterfaceIndexOrZero
_HpicfSrcIpAddrIfIndex_Object=MibTableColumn
hpicfSrcIpAddrIfIndex=_HpicfSrcIpAddrIfIndex_Object((1,3,6,1,4,1,11,2,14,11,1,13,1,1,1,4),_HpicfSrcIpAddrIfIndex_Type())
hpicfSrcIpAddrIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSrcIpAddrIfIndex.setStatus(_A)
_HpicfSrcIpAddress_Type=InetAddress
_HpicfSrcIpAddress_Object=MibTableColumn
hpicfSrcIpAddress=_HpicfSrcIpAddress_Object((1,3,6,1,4,1,11,2,14,11,1,13,1,1,1,5),_HpicfSrcIpAddress_Type())
hpicfSrcIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSrcIpAddress.setStatus(_A)
_HpicfSrcIpConformance_ObjectIdentity=ObjectIdentity
hpicfSrcIpConformance=_HpicfSrcIpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,13,2))
_HpicfSrcIpGroups_ObjectIdentity=ObjectIdentity
hpicfSrcIpGroups=_HpicfSrcIpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,13,2,1))
_HpicfSrcIpCompliances_ObjectIdentity=ObjectIdentity
hpicfSrcIpCompliances=_HpicfSrcIpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,13,2,2))
hpicfSrcIpBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,13,2,1,1))
hpicfSrcIpBaseGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:hpicfSrcIpBaseGroup.setStatus(_A)
hpicfSrcIpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,13,2,2,1))
hpicfSrcIpCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:hpicfSrcIpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfSrcIpMIB':hpicfSrcIpMIB,'hpicfSrcIpConfig':hpicfSrcIpConfig,'hpicfSrcIpAddrPolicyTable':hpicfSrcIpAddrPolicyTable,'hpicfSrcIpAddrPolicyEntry':hpicfSrcIpAddrPolicyEntry,_E:hpicfSrcIpAddressType,_F:hpicfSrcIpProtocolIndex,_H:hpicfSrcIpAddrPolicy,_I:hpicfSrcIpAddrIfIndex,_J:hpicfSrcIpAddress,'hpicfSrcIpConformance':hpicfSrcIpConformance,'hpicfSrcIpGroups':hpicfSrcIpGroups,_K:hpicfSrcIpBaseGroup,'hpicfSrcIpCompliances':hpicfSrcIpCompliances,'hpicfSrcIpCompliance':hpicfSrcIpCompliance})