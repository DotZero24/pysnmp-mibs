_S='natSyslogGroupVer1'
_R='natPortForwardingGroupVer1'
_Q='natSyslogEnable'
_P='natPortForwardingRuleEnable'
_O='natPortForwardingRuleLabel'
_N='natPortForwardingLanPort'
_M='natPortForwardingLanAddr'
_L='natPortForwardingProtocol'
_K='natPortForwardingWanFinishPort'
_J='natPortForwardingWanStartPort'
_I='natPortForwardingIndex'
_H='Unsigned32'
_G='Integer32'
_F='MxAdvancedIpPort'
_E='OctetString'
_D='MxEnableState'
_C='read-write'
_B='MX-NAT2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxAdvancedIpPort,MxEnableState,MxIpAddress,MxIpPort=mibBuilder.importSymbols('MX-TC',_F,_D,'MxIpAddress','MxIpPort')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
natMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,500))
if mibBuilder.loadTexts:natMIB.setRevisions(('2006-03-06 00:00','2005-04-19 00:00'))
_NatMIBObjects_ObjectIdentity=ObjectIdentity
natMIBObjects=_NatMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,500,1))
_NatPortForwarding_ObjectIdentity=ObjectIdentity
natPortForwarding=_NatPortForwarding_ObjectIdentity((1,3,6,1,4,1,4935,15,500,1,10))
_NatPortForwardingTable_Object=MibTable
natPortForwardingTable=_NatPortForwardingTable_Object((1,3,6,1,4,1,4935,15,500,1,10,10))
if mibBuilder.loadTexts:natPortForwardingTable.setStatus(_A)
_NatPortForwardingEntry_Object=MibTableRow
natPortForwardingEntry=_NatPortForwardingEntry_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5))
natPortForwardingEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:natPortForwardingEntry.setStatus(_A)
class _NatPortForwardingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_NatPortForwardingIndex_Type.__name__=_H
_NatPortForwardingIndex_Object=MibTableColumn
natPortForwardingIndex=_NatPortForwardingIndex_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,10),_NatPortForwardingIndex_Type())
natPortForwardingIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:natPortForwardingIndex.setStatus(_A)
_NatPortForwardingWanStartPort_Type=MxIpPort
_NatPortForwardingWanStartPort_Object=MibTableColumn
natPortForwardingWanStartPort=_NatPortForwardingWanStartPort_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,20),_NatPortForwardingWanStartPort_Type())
natPortForwardingWanStartPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortForwardingWanStartPort.setStatus(_A)
_NatPortForwardingWanFinishPort_Type=MxIpPort
_NatPortForwardingWanFinishPort_Object=MibTableColumn
natPortForwardingWanFinishPort=_NatPortForwardingWanFinishPort_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,30),_NatPortForwardingWanFinishPort_Type())
natPortForwardingWanFinishPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortForwardingWanFinishPort.setStatus(_A)
class _NatPortForwardingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,99)));namedValues=NamedValues(*(('udp',0),('tcp',1),('all',99)))
_NatPortForwardingProtocol_Type.__name__=_G
_NatPortForwardingProtocol_Object=MibTableColumn
natPortForwardingProtocol=_NatPortForwardingProtocol_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,40),_NatPortForwardingProtocol_Type())
natPortForwardingProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortForwardingProtocol.setStatus(_A)
_NatPortForwardingLanAddr_Type=MxIpAddress
_NatPortForwardingLanAddr_Object=MibTableColumn
natPortForwardingLanAddr=_NatPortForwardingLanAddr_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,50),_NatPortForwardingLanAddr_Type())
natPortForwardingLanAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortForwardingLanAddr.setStatus(_A)
class _NatPortForwardingLanPort_Type(MxAdvancedIpPort):defaultValue=0
_NatPortForwardingLanPort_Type.__name__=_F
_NatPortForwardingLanPort_Object=MibTableColumn
natPortForwardingLanPort=_NatPortForwardingLanPort_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,60),_NatPortForwardingLanPort_Type())
natPortForwardingLanPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortForwardingLanPort.setStatus(_A)
class _NatPortForwardingRuleLabel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NatPortForwardingRuleLabel_Type.__name__=_E
_NatPortForwardingRuleLabel_Object=MibTableColumn
natPortForwardingRuleLabel=_NatPortForwardingRuleLabel_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,70),_NatPortForwardingRuleLabel_Type())
natPortForwardingRuleLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortForwardingRuleLabel.setStatus(_A)
class _NatPortForwardingRuleEnable_Type(MxEnableState):defaultValue=0
_NatPortForwardingRuleEnable_Type.__name__=_D
_NatPortForwardingRuleEnable_Object=MibTableColumn
natPortForwardingRuleEnable=_NatPortForwardingRuleEnable_Object((1,3,6,1,4,1,4935,15,500,1,10,10,5,80),_NatPortForwardingRuleEnable_Type())
natPortForwardingRuleEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:natPortForwardingRuleEnable.setStatus(_A)
_NatSyslog_ObjectIdentity=ObjectIdentity
natSyslog=_NatSyslog_ObjectIdentity((1,3,6,1,4,1,4935,15,500,1,100))
class _NatSyslogEnable_Type(MxEnableState):defaultValue=0
_NatSyslogEnable_Type.__name__=_D
_NatSyslogEnable_Object=MibScalar
natSyslogEnable=_NatSyslogEnable_Object((1,3,6,1,4,1,4935,15,500,1,100,10),_NatSyslogEnable_Type())
natSyslogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:natSyslogEnable.setStatus(_A)
_NatConformance_ObjectIdentity=ObjectIdentity
natConformance=_NatConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,500,2))
_NatCompliances_ObjectIdentity=ObjectIdentity
natCompliances=_NatCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,500,2,1))
_NatGroups_ObjectIdentity=ObjectIdentity
natGroups=_NatGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,500,2,2))
natPortForwardingGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,500,2,2,1))
natPortForwardingGroupVer1.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:natPortForwardingGroupVer1.setStatus(_A)
natSyslogGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,500,2,2,2))
natSyslogGroupVer1.setObjects((_B,_Q))
if mibBuilder.loadTexts:natSyslogGroupVer1.setStatus(_A)
natComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,500,2,1,1))
natComplVer1.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:natComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'natMIB':natMIB,'natMIBObjects':natMIBObjects,'natPortForwarding':natPortForwarding,'natPortForwardingTable':natPortForwardingTable,'natPortForwardingEntry':natPortForwardingEntry,_I:natPortForwardingIndex,_J:natPortForwardingWanStartPort,_K:natPortForwardingWanFinishPort,_L:natPortForwardingProtocol,_M:natPortForwardingLanAddr,_N:natPortForwardingLanPort,_O:natPortForwardingRuleLabel,_P:natPortForwardingRuleEnable,'natSyslog':natSyslog,_Q:natSyslogEnable,'natConformance':natConformance,'natCompliances':natCompliances,'natComplVer1':natComplVer1,'natGroups':natGroups,_R:natPortForwardingGroupVer1,_S:natSyslogGroupVer1})