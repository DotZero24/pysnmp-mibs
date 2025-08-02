_K='sipUAConfigGroup'
_J='sipUACfgServerRole'
_I='sipUACfgServerAddress'
_H='sipUACfgServerAddressType'
_G='sipUACfgServerIndex'
_F='Unsigned32'
_E='applIndex'
_D='NETWORK-SERVICES-MIB'
_C='read-only'
_B='SIP-UA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
applIndex,=mibBuilder.importSymbols(_D,_E)
SipTCEntityRole,=mibBuilder.importSymbols('SIP-TC-MIB','SipTCEntityRole')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sipUAMIB=ModuleIdentity((1,3,6,1,2,1,150))
if mibBuilder.loadTexts:sipUAMIB.setRevisions(('2007-04-20 00:00',))
_SipUAMIBObjects_ObjectIdentity=ObjectIdentity
sipUAMIBObjects=_SipUAMIBObjects_ObjectIdentity((1,3,6,1,2,1,150,1))
_SipUACfgServer_ObjectIdentity=ObjectIdentity
sipUACfgServer=_SipUACfgServer_ObjectIdentity((1,3,6,1,2,1,150,1,1))
_SipUACfgServerTable_Object=MibTable
sipUACfgServerTable=_SipUACfgServerTable_Object((1,3,6,1,2,1,150,1,1,1))
if mibBuilder.loadTexts:sipUACfgServerTable.setStatus(_A)
_SipUACfgServerEntry_Object=MibTableRow
sipUACfgServerEntry=_SipUACfgServerEntry_Object((1,3,6,1,2,1,150,1,1,1,1))
sipUACfgServerEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:sipUACfgServerEntry.setStatus(_A)
class _SipUACfgServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SipUACfgServerIndex_Type.__name__=_F
_SipUACfgServerIndex_Object=MibTableColumn
sipUACfgServerIndex=_SipUACfgServerIndex_Object((1,3,6,1,2,1,150,1,1,1,1,1),_SipUACfgServerIndex_Type())
sipUACfgServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:sipUACfgServerIndex.setStatus(_A)
_SipUACfgServerAddressType_Type=InetAddressType
_SipUACfgServerAddressType_Object=MibTableColumn
sipUACfgServerAddressType=_SipUACfgServerAddressType_Object((1,3,6,1,2,1,150,1,1,1,1,2),_SipUACfgServerAddressType_Type())
sipUACfgServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:sipUACfgServerAddressType.setStatus(_A)
_SipUACfgServerAddress_Type=InetAddress
_SipUACfgServerAddress_Object=MibTableColumn
sipUACfgServerAddress=_SipUACfgServerAddress_Object((1,3,6,1,2,1,150,1,1,1,1,3),_SipUACfgServerAddress_Type())
sipUACfgServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sipUACfgServerAddress.setStatus(_A)
_SipUACfgServerRole_Type=SipTCEntityRole
_SipUACfgServerRole_Object=MibTableColumn
sipUACfgServerRole=_SipUACfgServerRole_Object((1,3,6,1,2,1,150,1,1,1,1,4),_SipUACfgServerRole_Type())
sipUACfgServerRole.setMaxAccess(_C)
if mibBuilder.loadTexts:sipUACfgServerRole.setStatus(_A)
_SipUAMIBConformance_ObjectIdentity=ObjectIdentity
sipUAMIBConformance=_SipUAMIBConformance_ObjectIdentity((1,3,6,1,2,1,150,2))
_SipUAMIBCompliances_ObjectIdentity=ObjectIdentity
sipUAMIBCompliances=_SipUAMIBCompliances_ObjectIdentity((1,3,6,1,2,1,150,2,1))
_SipUAMIBGroups_ObjectIdentity=ObjectIdentity
sipUAMIBGroups=_SipUAMIBGroups_ObjectIdentity((1,3,6,1,2,1,150,2,2))
sipUAConfigGroup=ObjectGroup((1,3,6,1,2,1,150,2,2,1))
sipUAConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:sipUAConfigGroup.setStatus(_A)
sipUACompliance=ModuleCompliance((1,3,6,1,2,1,150,2,1,1))
sipUACompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:sipUACompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sipUAMIB':sipUAMIB,'sipUAMIBObjects':sipUAMIBObjects,'sipUACfgServer':sipUACfgServer,'sipUACfgServerTable':sipUACfgServerTable,'sipUACfgServerEntry':sipUACfgServerEntry,_G:sipUACfgServerIndex,_H:sipUACfgServerAddressType,_I:sipUACfgServerAddress,_J:sipUACfgServerRole,'sipUAMIBConformance':sipUAMIBConformance,'sipUAMIBCompliances':sipUAMIBCompliances,'sipUACompliance':sipUACompliance,'sipUAMIBGroups':sipUAMIBGroups,_K:sipUAConfigGroup})