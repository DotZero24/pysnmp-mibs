_L='ntwsApIfBasicGroup'
_K='ntwsApIfMac'
_J='ntwsApIfHighSpeed'
_I='ntwsApIfMtu'
_H='ntwsApIfType'
_G='ntwsApIfName'
_F='not-accessible'
_E='ntwsApIfIndex'
_D='ntwsApIfApSerialNum'
_C='read-only'
_B='NTWS-AP-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
NtwsApSerialNum,=mibBuilder.importSymbols('NTWS-AP-TC','NtwsApSerialNum')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ntwsApIfMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,16))
if mibBuilder.loadTexts:ntwsApIfMib.setRevisions(('2008-11-20 00:01',))
class NtwsApInterfaceIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_NtwsApIfMibObjects_ObjectIdentity=ObjectIdentity
ntwsApIfMibObjects=_NtwsApIfMibObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,16,1))
_NtwsApIfTable_Object=MibTable
ntwsApIfTable=_NtwsApIfTable_Object((1,3,6,1,4,1,45,6,1,4,16,1,1))
if mibBuilder.loadTexts:ntwsApIfTable.setStatus(_A)
_NtwsApIfEntry_Object=MibTableRow
ntwsApIfEntry=_NtwsApIfEntry_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1))
ntwsApIfEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:ntwsApIfEntry.setStatus(_A)
_NtwsApIfApSerialNum_Type=NtwsApSerialNum
_NtwsApIfApSerialNum_Object=MibTableColumn
ntwsApIfApSerialNum=_NtwsApIfApSerialNum_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1,1),_NtwsApIfApSerialNum_Type())
ntwsApIfApSerialNum.setMaxAccess(_F)
if mibBuilder.loadTexts:ntwsApIfApSerialNum.setStatus(_A)
_NtwsApIfIndex_Type=NtwsApInterfaceIndex
_NtwsApIfIndex_Object=MibTableColumn
ntwsApIfIndex=_NtwsApIfIndex_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1,2),_NtwsApIfIndex_Type())
ntwsApIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ntwsApIfIndex.setStatus(_A)
_NtwsApIfName_Type=DisplayString
_NtwsApIfName_Object=MibTableColumn
ntwsApIfName=_NtwsApIfName_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1,3),_NtwsApIfName_Type())
ntwsApIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApIfName.setStatus(_A)
_NtwsApIfType_Type=IANAifType
_NtwsApIfType_Object=MibTableColumn
ntwsApIfType=_NtwsApIfType_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1,4),_NtwsApIfType_Type())
ntwsApIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApIfType.setStatus(_A)
_NtwsApIfMtu_Type=Unsigned32
_NtwsApIfMtu_Object=MibTableColumn
ntwsApIfMtu=_NtwsApIfMtu_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1,5),_NtwsApIfMtu_Type())
ntwsApIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApIfMtu.setStatus(_A)
_NtwsApIfHighSpeed_Type=Gauge32
_NtwsApIfHighSpeed_Object=MibTableColumn
ntwsApIfHighSpeed=_NtwsApIfHighSpeed_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1,6),_NtwsApIfHighSpeed_Type())
ntwsApIfHighSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApIfHighSpeed.setStatus(_A)
_NtwsApIfMac_Type=MacAddress
_NtwsApIfMac_Object=MibTableColumn
ntwsApIfMac=_NtwsApIfMac_Object((1,3,6,1,4,1,45,6,1,4,16,1,1,1,7),_NtwsApIfMac_Type())
ntwsApIfMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApIfMac.setStatus(_A)
_NtwsApIfConformance_ObjectIdentity=ObjectIdentity
ntwsApIfConformance=_NtwsApIfConformance_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,16,2))
_NtwsApIfCompliances_ObjectIdentity=ObjectIdentity
ntwsApIfCompliances=_NtwsApIfCompliances_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,16,2,1))
_NtwsApIfGroups_ObjectIdentity=ObjectIdentity
ntwsApIfGroups=_NtwsApIfGroups_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,16,2,2))
ntwsApIfBasicGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,16,2,2,1))
ntwsApIfBasicGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ntwsApIfBasicGroup.setStatus(_A)
ntwsApIfCompliance=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,16,2,1,1))
ntwsApIfCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ntwsApIfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NtwsApInterfaceIndex':NtwsApInterfaceIndex,'ntwsApIfMib':ntwsApIfMib,'ntwsApIfMibObjects':ntwsApIfMibObjects,'ntwsApIfTable':ntwsApIfTable,'ntwsApIfEntry':ntwsApIfEntry,_D:ntwsApIfApSerialNum,_E:ntwsApIfIndex,_G:ntwsApIfName,_H:ntwsApIfType,_I:ntwsApIfMtu,_J:ntwsApIfHighSpeed,_K:ntwsApIfMac,'ntwsApIfConformance':ntwsApIfConformance,'ntwsApIfCompliances':ntwsApIfCompliances,'ntwsApIfCompliance':ntwsApIfCompliance,'ntwsApIfGroups':ntwsApIfGroups,_L:ntwsApIfBasicGroup})