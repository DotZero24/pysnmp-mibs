_E='disable'
_D='enable'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathDenialOfService=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31))
if mibBuilder.loadTexts:fastPathDenialOfService.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
_AgentSwitchDenialOfServiceGroup_ObjectIdentity=ObjectIdentity
agentSwitchDenialOfServiceGroup=_AgentSwitchDenialOfServiceGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1))
class _AgentSwitchDenialOfServiceSIPDIPMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceSIPDIPMode_Type.__name__=_A
_AgentSwitchDenialOfServiceSIPDIPMode_Object=MibScalar
agentSwitchDenialOfServiceSIPDIPMode=_AgentSwitchDenialOfServiceSIPDIPMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,1),_AgentSwitchDenialOfServiceSIPDIPMode_Type())
agentSwitchDenialOfServiceSIPDIPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceSIPDIPMode.setStatus(_C)
class _AgentSwitchDenialOfServiceFirstFragMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceFirstFragMode_Type.__name__=_A
_AgentSwitchDenialOfServiceFirstFragMode_Object=MibScalar
agentSwitchDenialOfServiceFirstFragMode=_AgentSwitchDenialOfServiceFirstFragMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,2),_AgentSwitchDenialOfServiceFirstFragMode_Type())
agentSwitchDenialOfServiceFirstFragMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceFirstFragMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPHdrSize_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentSwitchDenialOfServiceTCPHdrSize_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPHdrSize_Object=MibScalar
agentSwitchDenialOfServiceTCPHdrSize=_AgentSwitchDenialOfServiceTCPHdrSize_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,3),_AgentSwitchDenialOfServiceTCPHdrSize_Type())
agentSwitchDenialOfServiceTCPHdrSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPHdrSize.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPFragMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPFragMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPFragMode_Object=MibScalar
agentSwitchDenialOfServiceTCPFragMode=_AgentSwitchDenialOfServiceTCPFragMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,4),_AgentSwitchDenialOfServiceTCPFragMode_Type())
agentSwitchDenialOfServiceTCPFragMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPFragMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPFlagMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPFlagMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPFlagMode_Object=MibScalar
agentSwitchDenialOfServiceTCPFlagMode=_AgentSwitchDenialOfServiceTCPFlagMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,5),_AgentSwitchDenialOfServiceTCPFlagMode_Type())
agentSwitchDenialOfServiceTCPFlagMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPFlagMode.setStatus(_C)
class _AgentSwitchDenialOfServiceL4PortMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceL4PortMode_Type.__name__=_A
_AgentSwitchDenialOfServiceL4PortMode_Object=MibScalar
agentSwitchDenialOfServiceL4PortMode=_AgentSwitchDenialOfServiceL4PortMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,6),_AgentSwitchDenialOfServiceL4PortMode_Type())
agentSwitchDenialOfServiceL4PortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceL4PortMode.setStatus(_C)
class _AgentSwitchDenialOfServiceICMPMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceICMPMode_Type.__name__=_A
_AgentSwitchDenialOfServiceICMPMode_Object=MibScalar
agentSwitchDenialOfServiceICMPMode=_AgentSwitchDenialOfServiceICMPMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,7),_AgentSwitchDenialOfServiceICMPMode_Type())
agentSwitchDenialOfServiceICMPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceICMPMode.setStatus(_C)
class _AgentSwitchDenialOfServiceICMPSize_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16376))
_AgentSwitchDenialOfServiceICMPSize_Type.__name__=_A
_AgentSwitchDenialOfServiceICMPSize_Object=MibScalar
agentSwitchDenialOfServiceICMPSize=_AgentSwitchDenialOfServiceICMPSize_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,8),_AgentSwitchDenialOfServiceICMPSize_Type())
agentSwitchDenialOfServiceICMPSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceICMPSize.setStatus(_C)
class _AgentSwitchDenialOfServiceSMACDMACMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceSMACDMACMode_Type.__name__=_A
_AgentSwitchDenialOfServiceSMACDMACMode_Object=MibScalar
agentSwitchDenialOfServiceSMACDMACMode=_AgentSwitchDenialOfServiceSMACDMACMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,9),_AgentSwitchDenialOfServiceSMACDMACMode_Type())
agentSwitchDenialOfServiceSMACDMACMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceSMACDMACMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPOffsetMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPOffsetMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPOffsetMode_Object=MibScalar
agentSwitchDenialOfServiceTCPOffsetMode=_AgentSwitchDenialOfServiceTCPOffsetMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,10),_AgentSwitchDenialOfServiceTCPOffsetMode_Type())
agentSwitchDenialOfServiceTCPOffsetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPOffsetMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPFlagSeqMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPFlagSeqMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPFlagSeqMode_Object=MibScalar
agentSwitchDenialOfServiceTCPFlagSeqMode=_AgentSwitchDenialOfServiceTCPFlagSeqMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,11),_AgentSwitchDenialOfServiceTCPFlagSeqMode_Type())
agentSwitchDenialOfServiceTCPFlagSeqMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPFlagSeqMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPPortMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPPortMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPPortMode_Object=MibScalar
agentSwitchDenialOfServiceTCPPortMode=_AgentSwitchDenialOfServiceTCPPortMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,12),_AgentSwitchDenialOfServiceTCPPortMode_Type())
agentSwitchDenialOfServiceTCPPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPPortMode.setStatus(_C)
class _AgentSwitchDenialOfServiceUDPPortMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceUDPPortMode_Type.__name__=_A
_AgentSwitchDenialOfServiceUDPPortMode_Object=MibScalar
agentSwitchDenialOfServiceUDPPortMode=_AgentSwitchDenialOfServiceUDPPortMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,13),_AgentSwitchDenialOfServiceUDPPortMode_Type())
agentSwitchDenialOfServiceUDPPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceUDPPortMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPSynMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPSynMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPSynMode_Object=MibScalar
agentSwitchDenialOfServiceTCPSynMode=_AgentSwitchDenialOfServiceTCPSynMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,14),_AgentSwitchDenialOfServiceTCPSynMode_Type())
agentSwitchDenialOfServiceTCPSynMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPSynMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPSynFinMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPSynFinMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPSynFinMode_Object=MibScalar
agentSwitchDenialOfServiceTCPSynFinMode=_AgentSwitchDenialOfServiceTCPSynFinMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,15),_AgentSwitchDenialOfServiceTCPSynFinMode_Type())
agentSwitchDenialOfServiceTCPSynFinMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPSynFinMode.setStatus(_C)
class _AgentSwitchDenialOfServiceTCPFinUrgPshMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceTCPFinUrgPshMode_Type.__name__=_A
_AgentSwitchDenialOfServiceTCPFinUrgPshMode_Object=MibScalar
agentSwitchDenialOfServiceTCPFinUrgPshMode=_AgentSwitchDenialOfServiceTCPFinUrgPshMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,16),_AgentSwitchDenialOfServiceTCPFinUrgPshMode_Type())
agentSwitchDenialOfServiceTCPFinUrgPshMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceTCPFinUrgPshMode.setStatus(_C)
class _AgentSwitchDenialOfServiceICMPv6Size_Type(Integer32):defaultValue=1023;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_AgentSwitchDenialOfServiceICMPv6Size_Type.__name__=_A
_AgentSwitchDenialOfServiceICMPv6Size_Object=MibScalar
agentSwitchDenialOfServiceICMPv6Size=_AgentSwitchDenialOfServiceICMPv6Size_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,18),_AgentSwitchDenialOfServiceICMPv6Size_Type())
agentSwitchDenialOfServiceICMPv6Size.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceICMPv6Size.setStatus(_C)
class _AgentSwitchDenialOfServiceICMPFragMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceICMPFragMode_Type.__name__=_A
_AgentSwitchDenialOfServiceICMPFragMode_Object=MibScalar
agentSwitchDenialOfServiceICMPFragMode=_AgentSwitchDenialOfServiceICMPFragMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,19),_AgentSwitchDenialOfServiceICMPFragMode_Type())
agentSwitchDenialOfServiceICMPFragMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceICMPFragMode.setStatus(_C)
class _AgentSwitchDenialOfServiceICMPv6Mode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServiceICMPv6Mode_Type.__name__=_A
_AgentSwitchDenialOfServiceICMPv6Mode_Object=MibScalar
agentSwitchDenialOfServiceICMPv6Mode=_AgentSwitchDenialOfServiceICMPv6Mode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,20),_AgentSwitchDenialOfServiceICMPv6Mode_Type())
agentSwitchDenialOfServiceICMPv6Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServiceICMPv6Mode.setStatus(_C)
class _AgentSwitchDenialOfServicePortDdisable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSwitchDenialOfServicePortDdisable_Type.__name__=_A
_AgentSwitchDenialOfServicePortDdisable_Object=MibScalar
agentSwitchDenialOfServicePortDdisable=_AgentSwitchDenialOfServicePortDdisable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,31,1,21),_AgentSwitchDenialOfServicePortDdisable_Type())
agentSwitchDenialOfServicePortDdisable.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchDenialOfServicePortDdisable.setStatus(_C)
mibBuilder.exportSymbols('DNOS-DENIALOFSERVICE-PRIVATE-MIB',**{'fastPathDenialOfService':fastPathDenialOfService,'agentSwitchDenialOfServiceGroup':agentSwitchDenialOfServiceGroup,'agentSwitchDenialOfServiceSIPDIPMode':agentSwitchDenialOfServiceSIPDIPMode,'agentSwitchDenialOfServiceFirstFragMode':agentSwitchDenialOfServiceFirstFragMode,'agentSwitchDenialOfServiceTCPHdrSize':agentSwitchDenialOfServiceTCPHdrSize,'agentSwitchDenialOfServiceTCPFragMode':agentSwitchDenialOfServiceTCPFragMode,'agentSwitchDenialOfServiceTCPFlagMode':agentSwitchDenialOfServiceTCPFlagMode,'agentSwitchDenialOfServiceL4PortMode':agentSwitchDenialOfServiceL4PortMode,'agentSwitchDenialOfServiceICMPMode':agentSwitchDenialOfServiceICMPMode,'agentSwitchDenialOfServiceICMPSize':agentSwitchDenialOfServiceICMPSize,'agentSwitchDenialOfServiceSMACDMACMode':agentSwitchDenialOfServiceSMACDMACMode,'agentSwitchDenialOfServiceTCPOffsetMode':agentSwitchDenialOfServiceTCPOffsetMode,'agentSwitchDenialOfServiceTCPFlagSeqMode':agentSwitchDenialOfServiceTCPFlagSeqMode,'agentSwitchDenialOfServiceTCPPortMode':agentSwitchDenialOfServiceTCPPortMode,'agentSwitchDenialOfServiceUDPPortMode':agentSwitchDenialOfServiceUDPPortMode,'agentSwitchDenialOfServiceTCPSynMode':agentSwitchDenialOfServiceTCPSynMode,'agentSwitchDenialOfServiceTCPSynFinMode':agentSwitchDenialOfServiceTCPSynFinMode,'agentSwitchDenialOfServiceTCPFinUrgPshMode':agentSwitchDenialOfServiceTCPFinUrgPshMode,'agentSwitchDenialOfServiceICMPv6Size':agentSwitchDenialOfServiceICMPv6Size,'agentSwitchDenialOfServiceICMPFragMode':agentSwitchDenialOfServiceICMPFragMode,'agentSwitchDenialOfServiceICMPv6Mode':agentSwitchDenialOfServiceICMPv6Mode,'agentSwitchDenialOfServicePortDdisable':agentSwitchDenialOfServicePortDdisable})