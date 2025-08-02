_G='nnsnmpTrapRcvrIndex'
_F='SNMP-MIB'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
nnsnmpMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,5))
if mibBuilder.loadTexts:nnsnmpMib.setRevisions(('1999-04-23 00:00',))
_NnsnmpObjects_ObjectIdentity=ObjectIdentity
nnsnmpObjects=_NnsnmpObjects_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,5,1))
class _NnsnmpAgentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('snmpV1',2),('snmpV2V1',3),('snmpV2cV1',4)))
_NnsnmpAgentType_Type.__name__=_B
_NnsnmpAgentType_Object=MibScalar
nnsnmpAgentType=_NnsnmpAgentType_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,1),_NnsnmpAgentType_Type())
nnsnmpAgentType.setMaxAccess(_D)
if mibBuilder.loadTexts:nnsnmpAgentType.setStatus(_A)
class _NnsnmpRmonSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),('not-supported',2)))
_NnsnmpRmonSupported_Type.__name__=_B
_NnsnmpRmonSupported_Object=MibScalar
nnsnmpRmonSupported=_NnsnmpRmonSupported_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,2),_NnsnmpRmonSupported_Type())
nnsnmpRmonSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:nnsnmpRmonSupported.setStatus(_A)
_NnsnmpSourceAddress_Type=IpAddress
_NnsnmpSourceAddress_Object=MibScalar
nnsnmpSourceAddress=_NnsnmpSourceAddress_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,3),_NnsnmpSourceAddress_Type())
nnsnmpSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsnmpSourceAddress.setStatus(_A)
_NnsnmpTrapRcvrTable_Object=MibTable
nnsnmpTrapRcvrTable=_NnsnmpTrapRcvrTable_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,4))
if mibBuilder.loadTexts:nnsnmpTrapRcvrTable.setStatus(_A)
_NnsnmpTrapRcvrEntry_Object=MibTableRow
nnsnmpTrapRcvrEntry=_NnsnmpTrapRcvrEntry_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,4,1))
nnsnmpTrapRcvrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nnsnmpTrapRcvrEntry.setStatus(_A)
_NnsnmpTrapRcvrIndex_Type=Integer32
_NnsnmpTrapRcvrIndex_Object=MibTableColumn
nnsnmpTrapRcvrIndex=_NnsnmpTrapRcvrIndex_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,4,1,1),_NnsnmpTrapRcvrIndex_Type())
nnsnmpTrapRcvrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nnsnmpTrapRcvrIndex.setStatus(_A)
class _NnsnmpTrapRcvrEntryStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_NnsnmpTrapRcvrEntryStatus_Type.__name__=_B
_NnsnmpTrapRcvrEntryStatus_Object=MibTableColumn
nnsnmpTrapRcvrEntryStatus=_NnsnmpTrapRcvrEntryStatus_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,4,1,2),_NnsnmpTrapRcvrEntryStatus_Type())
nnsnmpTrapRcvrEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsnmpTrapRcvrEntryStatus.setStatus(_A)
_NnsnmpTrapRcvrAddress_Type=IpAddress
_NnsnmpTrapRcvrAddress_Object=MibTableColumn
nnsnmpTrapRcvrAddress=_NnsnmpTrapRcvrAddress_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,4,1,3),_NnsnmpTrapRcvrAddress_Type())
nnsnmpTrapRcvrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsnmpTrapRcvrAddress.setStatus(_A)
class _NnsnmpTrapRcvrCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NnsnmpTrapRcvrCommunity_Type.__name__=_E
_NnsnmpTrapRcvrCommunity_Object=MibTableColumn
nnsnmpTrapRcvrCommunity=_NnsnmpTrapRcvrCommunity_Object((1,3,6,1,4,1,562,73,1,1,1,5,1,4,1,4),_NnsnmpTrapRcvrCommunity_Type())
nnsnmpTrapRcvrCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsnmpTrapRcvrCommunity.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'nnsnmpMib':nnsnmpMib,'nnsnmpObjects':nnsnmpObjects,'nnsnmpAgentType':nnsnmpAgentType,'nnsnmpRmonSupported':nnsnmpRmonSupported,'nnsnmpSourceAddress':nnsnmpSourceAddress,'nnsnmpTrapRcvrTable':nnsnmpTrapRcvrTable,'nnsnmpTrapRcvrEntry':nnsnmpTrapRcvrEntry,_G:nnsnmpTrapRcvrIndex,'nnsnmpTrapRcvrEntryStatus':nnsnmpTrapRcvrEntryStatus,'nnsnmpTrapRcvrAddress':nnsnmpTrapRcvrAddress,'nnsnmpTrapRcvrCommunity':nnsnmpTrapRcvrCommunity})