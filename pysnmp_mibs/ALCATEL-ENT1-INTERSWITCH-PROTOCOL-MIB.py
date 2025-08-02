_H='aipLLDPConfGroup'
_G='aipLLDPConfigNearestEdgeEnable'
_F='aipLLDPConfigManAddrTlvTxEnable'
_E='read-write'
_D='aipLLDPConfigManAddrPortNum'
_C='TruthValue'
_B='ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Aip,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Aip')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_C)
alcatelIND1InterswitchProtocolMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,9,1))
if mibBuilder.loadTexts:alcatelIND1InterswitchProtocolMIB.setRevisions(('2010-05-13 00:00','2007-04-03 00:00'))
_AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBObjects=_AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,9,1,1))
_AlcatelIND1InterswitchProtocolMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBNotifications=_AlcatelIND1InterswitchProtocolMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,9,1,1,0))
if mibBuilder.loadTexts:alcatelIND1InterswitchProtocolMIBNotifications.setStatus(_A)
_AipLLDPConfig_ObjectIdentity=ObjectIdentity
aipLLDPConfig=_AipLLDPConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,9,1,1,1))
_AipLLDPConfigManAddrTable_Object=MibTable
aipLLDPConfigManAddrTable=_AipLLDPConfigManAddrTable_Object((1,3,6,1,4,1,6486,801,1,2,1,9,1,1,1,1))
if mibBuilder.loadTexts:aipLLDPConfigManAddrTable.setStatus(_A)
_AipLLDPConfigManAddrEntry_Object=MibTableRow
aipLLDPConfigManAddrEntry=_AipLLDPConfigManAddrEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,9,1,1,1,1,1))
aipLLDPConfigManAddrEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:aipLLDPConfigManAddrEntry.setStatus(_A)
_AipLLDPConfigManAddrPortNum_Type=InterfaceIndex
_AipLLDPConfigManAddrPortNum_Object=MibTableColumn
aipLLDPConfigManAddrPortNum=_AipLLDPConfigManAddrPortNum_Object((1,3,6,1,4,1,6486,801,1,2,1,9,1,1,1,1,1,1),_AipLLDPConfigManAddrPortNum_Type())
aipLLDPConfigManAddrPortNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aipLLDPConfigManAddrPortNum.setStatus(_A)
class _AipLLDPConfigManAddrTlvTxEnable_Type(TruthValue):defaultValue=2
_AipLLDPConfigManAddrTlvTxEnable_Type.__name__=_C
_AipLLDPConfigManAddrTlvTxEnable_Object=MibTableColumn
aipLLDPConfigManAddrTlvTxEnable=_AipLLDPConfigManAddrTlvTxEnable_Object((1,3,6,1,4,1,6486,801,1,2,1,9,1,1,1,1,1,2),_AipLLDPConfigManAddrTlvTxEnable_Type())
aipLLDPConfigManAddrTlvTxEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:aipLLDPConfigManAddrTlvTxEnable.setStatus(_A)
class _AipLLDPConfigNearestEdgeEnable_Type(TruthValue):defaultValue=2
_AipLLDPConfigNearestEdgeEnable_Type.__name__=_C
_AipLLDPConfigNearestEdgeEnable_Object=MibScalar
aipLLDPConfigNearestEdgeEnable=_AipLLDPConfigNearestEdgeEnable_Object((1,3,6,1,4,1,6486,801,1,2,1,9,1,1,1,2),_AipLLDPConfigNearestEdgeEnable_Type())
aipLLDPConfigNearestEdgeEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:aipLLDPConfigNearestEdgeEnable.setStatus(_A)
_AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBConformance=_AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,9,1,2))
_AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBGroups=_AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,9,1,2,1))
_AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1InterswitchProtocolMIBCompliances=_AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,9,1,2,2))
aipLLDPConfGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,9,1,2,1,1))
aipLLDPConfGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:aipLLDPConfGroup.setStatus(_A)
alcatelIND1InterswitchProtocolMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,9,1,2,2,1))
alcatelIND1InterswitchProtocolMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:alcatelIND1InterswitchProtocolMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1InterswitchProtocolMIB':alcatelIND1InterswitchProtocolMIB,'alcatelIND1InterswitchProtocolMIBObjects':alcatelIND1InterswitchProtocolMIBObjects,'alcatelIND1InterswitchProtocolMIBNotifications':alcatelIND1InterswitchProtocolMIBNotifications,'aipLLDPConfig':aipLLDPConfig,'aipLLDPConfigManAddrTable':aipLLDPConfigManAddrTable,'aipLLDPConfigManAddrEntry':aipLLDPConfigManAddrEntry,_D:aipLLDPConfigManAddrPortNum,_F:aipLLDPConfigManAddrTlvTxEnable,_G:aipLLDPConfigNearestEdgeEnable,'alcatelIND1InterswitchProtocolMIBConformance':alcatelIND1InterswitchProtocolMIBConformance,'alcatelIND1InterswitchProtocolMIBGroups':alcatelIND1InterswitchProtocolMIBGroups,_H:aipLLDPConfGroup,'alcatelIND1InterswitchProtocolMIBCompliances':alcatelIND1InterswitchProtocolMIBCompliances,'alcatelIND1InterswitchProtocolMIBCompliance':alcatelIND1InterswitchProtocolMIBCompliance})