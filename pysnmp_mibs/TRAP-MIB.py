_F='trapIndex'
_E='TRAP-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctTrapTable,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctTrapTable')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Trap_ObjectIdentity=ObjectIdentity
trap=_Trap_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,7,1))
_TrapTable_Object=MibTable
trapTable=_TrapTable_Object((1,3,6,1,4,1,52,4,1,5,7,1,1))
if mibBuilder.loadTexts:trapTable.setStatus(_A)
_TrapEntry_Object=MibTableRow
trapEntry=_TrapEntry_Object((1,3,6,1,4,1,52,4,1,5,7,1,1,1))
trapEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:trapEntry.setStatus(_A)
class _TrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_TrapIndex_Type.__name__=_C
_TrapIndex_Object=MibTableColumn
trapIndex=_TrapIndex_Object((1,3,6,1,4,1,52,4,1,5,7,1,1,1,1),_TrapIndex_Type())
trapIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:trapIndex.setStatus(_A)
class _TrapCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TrapCommunityName_Type.__name__=_D
_TrapCommunityName_Object=MibTableColumn
trapCommunityName=_TrapCommunityName_Object((1,3,6,1,4,1,52,4,1,5,7,1,1,1,2),_TrapCommunityName_Type())
trapCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:trapCommunityName.setStatus(_A)
class _TrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trapsDisabled',1),('trapsEnabled',2)))
_TrapStatus_Type.__name__=_C
_TrapStatus_Object=MibTableColumn
trapStatus=_TrapStatus_Object((1,3,6,1,4,1,52,4,1,5,7,1,1,1,3),_TrapStatus_Type())
trapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:trapStatus.setStatus(_A)
_TrapIPAddr_Type=IpAddress
_TrapIPAddr_Object=MibTableColumn
trapIPAddr=_TrapIPAddr_Object((1,3,6,1,4,1,52,4,1,5,7,1,1,1,4),_TrapIPAddr_Type())
trapIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:trapIPAddr.setStatus(_A)
_TrapSrcParty_Type=ObjectIdentifier
_TrapSrcParty_Object=MibTableColumn
trapSrcParty=_TrapSrcParty_Object((1,3,6,1,4,1,52,4,1,5,7,1,1,1,5),_TrapSrcParty_Type())
trapSrcParty.setMaxAccess(_B)
if mibBuilder.loadTexts:trapSrcParty.setStatus(_A)
_TrapDstParty_Type=ObjectIdentifier
_TrapDstParty_Object=MibTableColumn
trapDstParty=_TrapDstParty_Object((1,3,6,1,4,1,52,4,1,5,7,1,1,1,6),_TrapDstParty_Type())
trapDstParty.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDstParty.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'trap':trap,'trapTable':trapTable,'trapEntry':trapEntry,_F:trapIndex,'trapCommunityName':trapCommunityName,'trapStatus':trapStatus,'trapIPAddr':trapIPAddr,'trapSrcParty':trapSrcParty,'trapDstParty':trapDstParty})