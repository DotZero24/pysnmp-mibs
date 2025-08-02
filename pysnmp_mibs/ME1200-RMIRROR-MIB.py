_g='me1200RmirrorConfigSessionPortTableInfoGroup'
_f='me1200RmirrorConfigSessionSourcePortTableInfoGroup'
_e='me1200RmirrorConfigSessionSourceVlanTableInfoGroup'
_d='me1200RmirrorConfigSessionSourceCpuTableInfoGroup'
_c='me1200RmirrorConfigSessionTableInfoGroup'
_b='me1200RmirrorCapabilitiesInfoGroup'
_a='me1200RmirrorConfigSessionPortType'
_Z='me1200RmirrorConfigSessionSourcePortMirrorType'
_Y='me1200RmirrorConfigSessionSourceVlanMode'
_X='me1200RmirrorConfigSessionSourceCpuMirrorType'
_W='me1200RmirrorConfigSessionVid'
_V='me1200RmirrorConfigSessionSwitchType'
_U='me1200RmirrorConfigSessionMode'
_T='me1200RmirrorCapabilitiesCpuMirrorSupport'
_S='me1200RmirrorCapabilitiesReflectorPortSupport'
_R='me1200RmirrorConfigSessionPortIfIndex'
_Q='me1200RmirrorConfigSessionPortSessionId'
_P='me1200RmirrorConfigSessionSourcePortIfIndex'
_O='me1200RmirrorConfigSessionSourcePortSessionId'
_N='me1200RmirrorConfigSessionSourceVlanIfIndex'
_M='me1200RmirrorConfigSessionSourceVlanSessionId'
_L='me1200RmirrorConfigSessionSourceCpuSwitchId'
_K='me1200RmirrorConfigSessionSourceCpuSessionId'
_J='me1200RmirrorConfigSessionSessionId'
_I='read-only'
_H='destination'
_G='intermediate'
_F='ME1200Unsigned16'
_E='read-write'
_D='Integer32'
_C='not-accessible'
_B='ME1200-RMIRROR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200InterfaceIndex,ME1200Unsigned16=mibBuilder.importSymbols('ME1200-TC','ME1200InterfaceIndex',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200RmirrorMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,120))
if mibBuilder.loadTexts:me1200RmirrorMib.setRevisions(('2014-05-08 00:00','2014-05-07 00:00'))
class ME1200RmirrorMirrorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('tx',1),('rx',2),('both',3)))
class ME1200RmirrorPortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),(_G,1),(_H,2),('reflector',3)))
class ME1200RmirrorSwitchType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('mirror',0),('source',1),(_G,2),(_H,3)))
_Me1200RmirrorMibObjects_ObjectIdentity=ObjectIdentity
me1200RmirrorMibObjects=_Me1200RmirrorMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,120,1))
_Me1200RmirrorCapabilities_ObjectIdentity=ObjectIdentity
me1200RmirrorCapabilities=_Me1200RmirrorCapabilities_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,120,1,1))
_Me1200RmirrorCapabilitiesReflectorPortSupport_Type=TruthValue
_Me1200RmirrorCapabilitiesReflectorPortSupport_Object=MibScalar
me1200RmirrorCapabilitiesReflectorPortSupport=_Me1200RmirrorCapabilitiesReflectorPortSupport_Object((1,3,6,1,4,1,9,9,815,1,120,1,1,1),_Me1200RmirrorCapabilitiesReflectorPortSupport_Type())
me1200RmirrorCapabilitiesReflectorPortSupport.setMaxAccess(_I)
if mibBuilder.loadTexts:me1200RmirrorCapabilitiesReflectorPortSupport.setStatus(_A)
_Me1200RmirrorCapabilitiesCpuMirrorSupport_Type=TruthValue
_Me1200RmirrorCapabilitiesCpuMirrorSupport_Object=MibScalar
me1200RmirrorCapabilitiesCpuMirrorSupport=_Me1200RmirrorCapabilitiesCpuMirrorSupport_Object((1,3,6,1,4,1,9,9,815,1,120,1,1,2),_Me1200RmirrorCapabilitiesCpuMirrorSupport_Type())
me1200RmirrorCapabilitiesCpuMirrorSupport.setMaxAccess(_I)
if mibBuilder.loadTexts:me1200RmirrorCapabilitiesCpuMirrorSupport.setStatus(_A)
_Me1200RmirrorConfig_ObjectIdentity=ObjectIdentity
me1200RmirrorConfig=_Me1200RmirrorConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,120,1,2))
_Me1200RmirrorConfigSessionTable_Object=MibTable
me1200RmirrorConfigSessionTable=_Me1200RmirrorConfigSessionTable_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,1))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionTable.setStatus(_A)
_Me1200RmirrorConfigSessionEntry_Object=MibTableRow
me1200RmirrorConfigSessionEntry=_Me1200RmirrorConfigSessionEntry_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,1,1))
me1200RmirrorConfigSessionEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionEntry.setStatus(_A)
class _Me1200RmirrorConfigSessionSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Me1200RmirrorConfigSessionSessionId_Type.__name__=_D
_Me1200RmirrorConfigSessionSessionId_Object=MibTableColumn
me1200RmirrorConfigSessionSessionId=_Me1200RmirrorConfigSessionSessionId_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,1,1,1),_Me1200RmirrorConfigSessionSessionId_Type())
me1200RmirrorConfigSessionSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSessionId.setStatus(_A)
_Me1200RmirrorConfigSessionMode_Type=TruthValue
_Me1200RmirrorConfigSessionMode_Object=MibTableColumn
me1200RmirrorConfigSessionMode=_Me1200RmirrorConfigSessionMode_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,1,1,2),_Me1200RmirrorConfigSessionMode_Type())
me1200RmirrorConfigSessionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionMode.setStatus(_A)
_Me1200RmirrorConfigSessionSwitchType_Type=ME1200RmirrorSwitchType
_Me1200RmirrorConfigSessionSwitchType_Object=MibTableColumn
me1200RmirrorConfigSessionSwitchType=_Me1200RmirrorConfigSessionSwitchType_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,1,1,3),_Me1200RmirrorConfigSessionSwitchType_Type())
me1200RmirrorConfigSessionSwitchType.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSwitchType.setStatus(_A)
class _Me1200RmirrorConfigSessionVid_Type(ME1200Unsigned16):subtypeSpec=ME1200Unsigned16.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_Me1200RmirrorConfigSessionVid_Type.__name__=_F
_Me1200RmirrorConfigSessionVid_Object=MibTableColumn
me1200RmirrorConfigSessionVid=_Me1200RmirrorConfigSessionVid_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,1,1,4),_Me1200RmirrorConfigSessionVid_Type())
me1200RmirrorConfigSessionVid.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionVid.setStatus(_A)
_Me1200RmirrorConfigSessionSourceCpuTable_Object=MibTable
me1200RmirrorConfigSessionSourceCpuTable=_Me1200RmirrorConfigSessionSourceCpuTable_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,2))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceCpuTable.setStatus(_A)
_Me1200RmirrorConfigSessionSourceCpuEntry_Object=MibTableRow
me1200RmirrorConfigSessionSourceCpuEntry=_Me1200RmirrorConfigSessionSourceCpuEntry_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,2,1))
me1200RmirrorConfigSessionSourceCpuEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceCpuEntry.setStatus(_A)
class _Me1200RmirrorConfigSessionSourceCpuSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Me1200RmirrorConfigSessionSourceCpuSessionId_Type.__name__=_D
_Me1200RmirrorConfigSessionSourceCpuSessionId_Object=MibTableColumn
me1200RmirrorConfigSessionSourceCpuSessionId=_Me1200RmirrorConfigSessionSourceCpuSessionId_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,2,1,1),_Me1200RmirrorConfigSessionSourceCpuSessionId_Type())
me1200RmirrorConfigSessionSourceCpuSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceCpuSessionId.setStatus(_A)
class _Me1200RmirrorConfigSessionSourceCpuSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Me1200RmirrorConfigSessionSourceCpuSwitchId_Type.__name__=_D
_Me1200RmirrorConfigSessionSourceCpuSwitchId_Object=MibTableColumn
me1200RmirrorConfigSessionSourceCpuSwitchId=_Me1200RmirrorConfigSessionSourceCpuSwitchId_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,2,1,2),_Me1200RmirrorConfigSessionSourceCpuSwitchId_Type())
me1200RmirrorConfigSessionSourceCpuSwitchId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceCpuSwitchId.setStatus(_A)
_Me1200RmirrorConfigSessionSourceCpuMirrorType_Type=ME1200RmirrorMirrorType
_Me1200RmirrorConfigSessionSourceCpuMirrorType_Object=MibTableColumn
me1200RmirrorConfigSessionSourceCpuMirrorType=_Me1200RmirrorConfigSessionSourceCpuMirrorType_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,2,1,3),_Me1200RmirrorConfigSessionSourceCpuMirrorType_Type())
me1200RmirrorConfigSessionSourceCpuMirrorType.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceCpuMirrorType.setStatus(_A)
_Me1200RmirrorConfigSessionSourceVlanTable_Object=MibTable
me1200RmirrorConfigSessionSourceVlanTable=_Me1200RmirrorConfigSessionSourceVlanTable_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,3))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceVlanTable.setStatus(_A)
_Me1200RmirrorConfigSessionSourceVlanEntry_Object=MibTableRow
me1200RmirrorConfigSessionSourceVlanEntry=_Me1200RmirrorConfigSessionSourceVlanEntry_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,3,1))
me1200RmirrorConfigSessionSourceVlanEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceVlanEntry.setStatus(_A)
class _Me1200RmirrorConfigSessionSourceVlanSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Me1200RmirrorConfigSessionSourceVlanSessionId_Type.__name__=_D
_Me1200RmirrorConfigSessionSourceVlanSessionId_Object=MibTableColumn
me1200RmirrorConfigSessionSourceVlanSessionId=_Me1200RmirrorConfigSessionSourceVlanSessionId_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,3,1,1),_Me1200RmirrorConfigSessionSourceVlanSessionId_Type())
me1200RmirrorConfigSessionSourceVlanSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceVlanSessionId.setStatus(_A)
_Me1200RmirrorConfigSessionSourceVlanIfIndex_Type=ME1200InterfaceIndex
_Me1200RmirrorConfigSessionSourceVlanIfIndex_Object=MibTableColumn
me1200RmirrorConfigSessionSourceVlanIfIndex=_Me1200RmirrorConfigSessionSourceVlanIfIndex_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,3,1,2),_Me1200RmirrorConfigSessionSourceVlanIfIndex_Type())
me1200RmirrorConfigSessionSourceVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceVlanIfIndex.setStatus(_A)
_Me1200RmirrorConfigSessionSourceVlanMode_Type=TruthValue
_Me1200RmirrorConfigSessionSourceVlanMode_Object=MibTableColumn
me1200RmirrorConfigSessionSourceVlanMode=_Me1200RmirrorConfigSessionSourceVlanMode_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,3,1,3),_Me1200RmirrorConfigSessionSourceVlanMode_Type())
me1200RmirrorConfigSessionSourceVlanMode.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceVlanMode.setStatus(_A)
_Me1200RmirrorConfigSessionSourcePortTable_Object=MibTable
me1200RmirrorConfigSessionSourcePortTable=_Me1200RmirrorConfigSessionSourcePortTable_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,4))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourcePortTable.setStatus(_A)
_Me1200RmirrorConfigSessionSourcePortEntry_Object=MibTableRow
me1200RmirrorConfigSessionSourcePortEntry=_Me1200RmirrorConfigSessionSourcePortEntry_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,4,1))
me1200RmirrorConfigSessionSourcePortEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourcePortEntry.setStatus(_A)
class _Me1200RmirrorConfigSessionSourcePortSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Me1200RmirrorConfigSessionSourcePortSessionId_Type.__name__=_D
_Me1200RmirrorConfigSessionSourcePortSessionId_Object=MibTableColumn
me1200RmirrorConfigSessionSourcePortSessionId=_Me1200RmirrorConfigSessionSourcePortSessionId_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,4,1,1),_Me1200RmirrorConfigSessionSourcePortSessionId_Type())
me1200RmirrorConfigSessionSourcePortSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourcePortSessionId.setStatus(_A)
_Me1200RmirrorConfigSessionSourcePortIfIndex_Type=ME1200InterfaceIndex
_Me1200RmirrorConfigSessionSourcePortIfIndex_Object=MibTableColumn
me1200RmirrorConfigSessionSourcePortIfIndex=_Me1200RmirrorConfigSessionSourcePortIfIndex_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,4,1,2),_Me1200RmirrorConfigSessionSourcePortIfIndex_Type())
me1200RmirrorConfigSessionSourcePortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourcePortIfIndex.setStatus(_A)
_Me1200RmirrorConfigSessionSourcePortMirrorType_Type=ME1200RmirrorMirrorType
_Me1200RmirrorConfigSessionSourcePortMirrorType_Object=MibTableColumn
me1200RmirrorConfigSessionSourcePortMirrorType=_Me1200RmirrorConfigSessionSourcePortMirrorType_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,4,1,3),_Me1200RmirrorConfigSessionSourcePortMirrorType_Type())
me1200RmirrorConfigSessionSourcePortMirrorType.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourcePortMirrorType.setStatus(_A)
_Me1200RmirrorConfigSessionPortTable_Object=MibTable
me1200RmirrorConfigSessionPortTable=_Me1200RmirrorConfigSessionPortTable_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,5))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionPortTable.setStatus(_A)
_Me1200RmirrorConfigSessionPortEntry_Object=MibTableRow
me1200RmirrorConfigSessionPortEntry=_Me1200RmirrorConfigSessionPortEntry_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,5,1))
me1200RmirrorConfigSessionPortEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionPortEntry.setStatus(_A)
class _Me1200RmirrorConfigSessionPortSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Me1200RmirrorConfigSessionPortSessionId_Type.__name__=_D
_Me1200RmirrorConfigSessionPortSessionId_Object=MibTableColumn
me1200RmirrorConfigSessionPortSessionId=_Me1200RmirrorConfigSessionPortSessionId_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,5,1,1),_Me1200RmirrorConfigSessionPortSessionId_Type())
me1200RmirrorConfigSessionPortSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionPortSessionId.setStatus(_A)
_Me1200RmirrorConfigSessionPortIfIndex_Type=ME1200InterfaceIndex
_Me1200RmirrorConfigSessionPortIfIndex_Object=MibTableColumn
me1200RmirrorConfigSessionPortIfIndex=_Me1200RmirrorConfigSessionPortIfIndex_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,5,1,2),_Me1200RmirrorConfigSessionPortIfIndex_Type())
me1200RmirrorConfigSessionPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionPortIfIndex.setStatus(_A)
_Me1200RmirrorConfigSessionPortType_Type=ME1200RmirrorPortType
_Me1200RmirrorConfigSessionPortType_Object=MibTableColumn
me1200RmirrorConfigSessionPortType=_Me1200RmirrorConfigSessionPortType_Object((1,3,6,1,4,1,9,9,815,1,120,1,2,5,1,3),_Me1200RmirrorConfigSessionPortType_Type())
me1200RmirrorConfigSessionPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200RmirrorConfigSessionPortType.setStatus(_A)
_Me1200RmirrorMibConformance_ObjectIdentity=ObjectIdentity
me1200RmirrorMibConformance=_Me1200RmirrorMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,120,2))
_Me1200RmirrorMibCompliances_ObjectIdentity=ObjectIdentity
me1200RmirrorMibCompliances=_Me1200RmirrorMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,120,2,1))
_Me1200RmirrorMibGroups_ObjectIdentity=ObjectIdentity
me1200RmirrorMibGroups=_Me1200RmirrorMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,120,2,2))
me1200RmirrorCapabilitiesInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,120,2,2,1))
me1200RmirrorCapabilitiesInfoGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:me1200RmirrorCapabilitiesInfoGroup.setStatus(_A)
me1200RmirrorConfigSessionTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,120,2,2,2))
me1200RmirrorConfigSessionTableInfoGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionTableInfoGroup.setStatus(_A)
me1200RmirrorConfigSessionSourceCpuTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,120,2,2,3))
me1200RmirrorConfigSessionSourceCpuTableInfoGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceCpuTableInfoGroup.setStatus(_A)
me1200RmirrorConfigSessionSourceVlanTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,120,2,2,4))
me1200RmirrorConfigSessionSourceVlanTableInfoGroup.setObjects((_B,_Y))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourceVlanTableInfoGroup.setStatus(_A)
me1200RmirrorConfigSessionSourcePortTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,120,2,2,5))
me1200RmirrorConfigSessionSourcePortTableInfoGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionSourcePortTableInfoGroup.setStatus(_A)
me1200RmirrorConfigSessionPortTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,120,2,2,6))
me1200RmirrorConfigSessionPortTableInfoGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:me1200RmirrorConfigSessionPortTableInfoGroup.setStatus(_A)
me1200RmirrorMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,120,2,1,1))
me1200RmirrorMibCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:me1200RmirrorMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200RmirrorMirrorType':ME1200RmirrorMirrorType,'ME1200RmirrorPortType':ME1200RmirrorPortType,'ME1200RmirrorSwitchType':ME1200RmirrorSwitchType,'me1200RmirrorMib':me1200RmirrorMib,'me1200RmirrorMibObjects':me1200RmirrorMibObjects,'me1200RmirrorCapabilities':me1200RmirrorCapabilities,_S:me1200RmirrorCapabilitiesReflectorPortSupport,_T:me1200RmirrorCapabilitiesCpuMirrorSupport,'me1200RmirrorConfig':me1200RmirrorConfig,'me1200RmirrorConfigSessionTable':me1200RmirrorConfigSessionTable,'me1200RmirrorConfigSessionEntry':me1200RmirrorConfigSessionEntry,_J:me1200RmirrorConfigSessionSessionId,_U:me1200RmirrorConfigSessionMode,_V:me1200RmirrorConfigSessionSwitchType,_W:me1200RmirrorConfigSessionVid,'me1200RmirrorConfigSessionSourceCpuTable':me1200RmirrorConfigSessionSourceCpuTable,'me1200RmirrorConfigSessionSourceCpuEntry':me1200RmirrorConfigSessionSourceCpuEntry,_K:me1200RmirrorConfigSessionSourceCpuSessionId,_L:me1200RmirrorConfigSessionSourceCpuSwitchId,_X:me1200RmirrorConfigSessionSourceCpuMirrorType,'me1200RmirrorConfigSessionSourceVlanTable':me1200RmirrorConfigSessionSourceVlanTable,'me1200RmirrorConfigSessionSourceVlanEntry':me1200RmirrorConfigSessionSourceVlanEntry,_M:me1200RmirrorConfigSessionSourceVlanSessionId,_N:me1200RmirrorConfigSessionSourceVlanIfIndex,_Y:me1200RmirrorConfigSessionSourceVlanMode,'me1200RmirrorConfigSessionSourcePortTable':me1200RmirrorConfigSessionSourcePortTable,'me1200RmirrorConfigSessionSourcePortEntry':me1200RmirrorConfigSessionSourcePortEntry,_O:me1200RmirrorConfigSessionSourcePortSessionId,_P:me1200RmirrorConfigSessionSourcePortIfIndex,_Z:me1200RmirrorConfigSessionSourcePortMirrorType,'me1200RmirrorConfigSessionPortTable':me1200RmirrorConfigSessionPortTable,'me1200RmirrorConfigSessionPortEntry':me1200RmirrorConfigSessionPortEntry,_Q:me1200RmirrorConfigSessionPortSessionId,_R:me1200RmirrorConfigSessionPortIfIndex,_a:me1200RmirrorConfigSessionPortType,'me1200RmirrorMibConformance':me1200RmirrorMibConformance,'me1200RmirrorMibCompliances':me1200RmirrorMibCompliances,'me1200RmirrorMibCompliance':me1200RmirrorMibCompliance,'me1200RmirrorMibGroups':me1200RmirrorMibGroups,_b:me1200RmirrorCapabilitiesInfoGroup,_c:me1200RmirrorConfigSessionTableInfoGroup,_d:me1200RmirrorConfigSessionSourceCpuTableInfoGroup,_e:me1200RmirrorConfigSessionSourceVlanTableInfoGroup,_f:me1200RmirrorConfigSessionSourcePortTableInfoGroup,_g:me1200RmirrorConfigSessionPortTableInfoGroup})