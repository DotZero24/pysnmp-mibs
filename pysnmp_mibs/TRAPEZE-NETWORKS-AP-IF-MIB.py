_L='trpzApIfBasicGroup'
_K='trpzApIfMac'
_J='trpzApIfHighSpeed'
_I='trpzApIfMtu'
_H='trpzApIfType'
_G='trpzApIfName'
_F='not-accessible'
_E='trpzApIfIndex'
_D='trpzApIfApSerialNum'
_C='read-only'
_B='TRAPEZE-NETWORKS-AP-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
TrpzApSerialNum,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-AP-TC','TrpzApSerialNum')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzApIfMib=ModuleIdentity((1,3,6,1,4,1,14525,4,16))
if mibBuilder.loadTexts:trpzApIfMib.setRevisions(('2008-11-20 00:01',))
class TrpzApInterfaceIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_TrpzApIfMibObjects_ObjectIdentity=ObjectIdentity
trpzApIfMibObjects=_TrpzApIfMibObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,16,1))
_TrpzApIfTable_Object=MibTable
trpzApIfTable=_TrpzApIfTable_Object((1,3,6,1,4,1,14525,4,16,1,1))
if mibBuilder.loadTexts:trpzApIfTable.setStatus(_A)
_TrpzApIfEntry_Object=MibTableRow
trpzApIfEntry=_TrpzApIfEntry_Object((1,3,6,1,4,1,14525,4,16,1,1,1))
trpzApIfEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:trpzApIfEntry.setStatus(_A)
_TrpzApIfApSerialNum_Type=TrpzApSerialNum
_TrpzApIfApSerialNum_Object=MibTableColumn
trpzApIfApSerialNum=_TrpzApIfApSerialNum_Object((1,3,6,1,4,1,14525,4,16,1,1,1,1),_TrpzApIfApSerialNum_Type())
trpzApIfApSerialNum.setMaxAccess(_F)
if mibBuilder.loadTexts:trpzApIfApSerialNum.setStatus(_A)
_TrpzApIfIndex_Type=TrpzApInterfaceIndex
_TrpzApIfIndex_Object=MibTableColumn
trpzApIfIndex=_TrpzApIfIndex_Object((1,3,6,1,4,1,14525,4,16,1,1,1,2),_TrpzApIfIndex_Type())
trpzApIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:trpzApIfIndex.setStatus(_A)
_TrpzApIfName_Type=DisplayString
_TrpzApIfName_Object=MibTableColumn
trpzApIfName=_TrpzApIfName_Object((1,3,6,1,4,1,14525,4,16,1,1,1,3),_TrpzApIfName_Type())
trpzApIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApIfName.setStatus(_A)
_TrpzApIfType_Type=IANAifType
_TrpzApIfType_Object=MibTableColumn
trpzApIfType=_TrpzApIfType_Object((1,3,6,1,4,1,14525,4,16,1,1,1,4),_TrpzApIfType_Type())
trpzApIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApIfType.setStatus(_A)
_TrpzApIfMtu_Type=Unsigned32
_TrpzApIfMtu_Object=MibTableColumn
trpzApIfMtu=_TrpzApIfMtu_Object((1,3,6,1,4,1,14525,4,16,1,1,1,5),_TrpzApIfMtu_Type())
trpzApIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApIfMtu.setStatus(_A)
_TrpzApIfHighSpeed_Type=Gauge32
_TrpzApIfHighSpeed_Object=MibTableColumn
trpzApIfHighSpeed=_TrpzApIfHighSpeed_Object((1,3,6,1,4,1,14525,4,16,1,1,1,6),_TrpzApIfHighSpeed_Type())
trpzApIfHighSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApIfHighSpeed.setStatus(_A)
_TrpzApIfMac_Type=MacAddress
_TrpzApIfMac_Object=MibTableColumn
trpzApIfMac=_TrpzApIfMac_Object((1,3,6,1,4,1,14525,4,16,1,1,1,7),_TrpzApIfMac_Type())
trpzApIfMac.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzApIfMac.setStatus(_A)
_TrpzApIfConformance_ObjectIdentity=ObjectIdentity
trpzApIfConformance=_TrpzApIfConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,16,2))
_TrpzApIfCompliances_ObjectIdentity=ObjectIdentity
trpzApIfCompliances=_TrpzApIfCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,16,2,1))
_TrpzApIfGroups_ObjectIdentity=ObjectIdentity
trpzApIfGroups=_TrpzApIfGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,16,2,2))
trpzApIfBasicGroup=ObjectGroup((1,3,6,1,4,1,14525,4,16,2,2,1))
trpzApIfBasicGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:trpzApIfBasicGroup.setStatus(_A)
trpzApIfCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,16,2,1,1))
trpzApIfCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:trpzApIfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TrpzApInterfaceIndex':TrpzApInterfaceIndex,'trpzApIfMib':trpzApIfMib,'trpzApIfMibObjects':trpzApIfMibObjects,'trpzApIfTable':trpzApIfTable,'trpzApIfEntry':trpzApIfEntry,_D:trpzApIfApSerialNum,_E:trpzApIfIndex,_G:trpzApIfName,_H:trpzApIfType,_I:trpzApIfMtu,_J:trpzApIfHighSpeed,_K:trpzApIfMac,'trpzApIfConformance':trpzApIfConformance,'trpzApIfCompliances':trpzApIfCompliances,'trpzApIfCompliance':trpzApIfCompliance,'trpzApIfGroups':trpzApIfGroups,_L:trpzApIfBasicGroup})