_o='osModuleLteOptGroup'
_n='osModuleLteGroup'
_m='osModFiveGApnDevAdminStatus'
_l='osModFiveGApnDevDefault'
_k='osModFiveGApnDevBand'
_j='osModFiveGApnDevProtocol'
_i='osModFiveGApnDevID'
_h='osModFiveGApnDevPriority'
_g='osModFiveGApnModLastActive'
_f='osModFiveGApnModBand'
_e='osModFiveGApnModProtocol'
_d='osModFiveGApnModID'
_c='osModFiveGApnModPriority'
_b='osModLteApnDevAdminStatus'
_a='osModLteApnDevDefault'
_Z='osModLteApnDevBand'
_Y='osModLteApnDevProtocol'
_X='osModLteApnDevID'
_W='osModLteApnDevPriority'
_V='osModLteApnModLastActive'
_U='osModLteApnModBand'
_T='osModLteApnModProtocol'
_S='osModLteApnModID'
_R='osModLteApnModPriority'
_Q='osModFiveGApnDevName'
_P='osModFiveGApnModName'
_O='osModLteApnDevName'
_N='osModLteApnModName'
_M='osModuleLteSupport'
_L='ipv4ipv6'
_K='ipv6'
_J='ipv4'
_I='unknown'
_H='not-accessible'
_G='DisplayString'
_F='Integer32'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='OS-MODULE-LTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntityName,EntryValidator,oaOptiSwitch=mibBuilder.importSymbols('OS-COMMON-TC-MIB','EntityName','EntryValidator','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
osModuleLte=ModuleIdentity((1,3,6,1,4,1,6926,2,42))
if mibBuilder.loadTexts:osModuleLte.setRevisions(('2023-01-26 00:00','2020-09-16 00:00'))
_OsModuleLteGen_ObjectIdentity=ObjectIdentity
osModuleLteGen=_OsModuleLteGen_ObjectIdentity((1,3,6,1,4,1,6926,2,42,1))
class _OsModuleLteSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsModuleLteSupport_Type.__name__=_F
_OsModuleLteSupport_Object=MibScalar
osModuleLteSupport=_OsModuleLteSupport_Object((1,3,6,1,4,1,6926,2,42,1,1),_OsModuleLteSupport_Type())
osModuleLteSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleLteSupport.setStatus(_A)
_OsModuleLteTables_ObjectIdentity=ObjectIdentity
osModuleLteTables=_OsModuleLteTables_ObjectIdentity((1,3,6,1,4,1,6926,2,42,2))
_OsModLteApnModTable_Object=MibTable
osModLteApnModTable=_OsModLteApnModTable_Object((1,3,6,1,4,1,6926,2,42,2,1))
if mibBuilder.loadTexts:osModLteApnModTable.setStatus(_A)
_OsModLteApnModEntry_Object=MibTableRow
osModLteApnModEntry=_OsModLteApnModEntry_Object((1,3,6,1,4,1,6926,2,42,2,1,1))
osModLteApnModEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:osModLteApnModEntry.setStatus(_A)
_OsModLteApnModName_Type=EntityName
_OsModLteApnModName_Object=MibTableColumn
osModLteApnModName=_OsModLteApnModName_Object((1,3,6,1,4,1,6926,2,42,2,1,1,2),_OsModLteApnModName_Type())
osModLteApnModName.setMaxAccess(_H)
if mibBuilder.loadTexts:osModLteApnModName.setStatus(_A)
class _OsModLteApnModPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_OsModLteApnModPriority_Type.__name__=_E
_OsModLteApnModPriority_Object=MibTableColumn
osModLteApnModPriority=_OsModLteApnModPriority_Object((1,3,6,1,4,1,6926,2,42,2,1,1,3),_OsModLteApnModPriority_Type())
osModLteApnModPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:osModLteApnModPriority.setStatus(_A)
class _OsModLteApnModID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,63))
_OsModLteApnModID_Type.__name__=_G
_OsModLteApnModID_Object=MibTableColumn
osModLteApnModID=_OsModLteApnModID_Object((1,3,6,1,4,1,6926,2,42,2,1,1,4),_OsModLteApnModID_Type())
osModLteApnModID.setMaxAccess(_C)
if mibBuilder.loadTexts:osModLteApnModID.setStatus(_A)
class _OsModLteApnModProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3)))
_OsModLteApnModProtocol_Type.__name__=_F
_OsModLteApnModProtocol_Object=MibTableColumn
osModLteApnModProtocol=_OsModLteApnModProtocol_Object((1,3,6,1,4,1,6926,2,42,2,1,1,5),_OsModLteApnModProtocol_Type())
osModLteApnModProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:osModLteApnModProtocol.setStatus(_A)
class _OsModLteApnModBand_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_OsModLteApnModBand_Type.__name__=_E
_OsModLteApnModBand_Object=MibTableColumn
osModLteApnModBand=_OsModLteApnModBand_Object((1,3,6,1,4,1,6926,2,42,2,1,1,6),_OsModLteApnModBand_Type())
osModLteApnModBand.setMaxAccess(_C)
if mibBuilder.loadTexts:osModLteApnModBand.setStatus(_A)
_OsModLteApnModLastActive_Type=TruthValue
_OsModLteApnModLastActive_Object=MibTableColumn
osModLteApnModLastActive=_OsModLteApnModLastActive_Object((1,3,6,1,4,1,6926,2,42,2,1,1,7),_OsModLteApnModLastActive_Type())
osModLteApnModLastActive.setMaxAccess(_C)
if mibBuilder.loadTexts:osModLteApnModLastActive.setStatus(_A)
_OsModLteApnDevTable_Object=MibTable
osModLteApnDevTable=_OsModLteApnDevTable_Object((1,3,6,1,4,1,6926,2,42,2,2))
if mibBuilder.loadTexts:osModLteApnDevTable.setStatus(_A)
_OsModLteApnDevEntry_Object=MibTableRow
osModLteApnDevEntry=_OsModLteApnDevEntry_Object((1,3,6,1,4,1,6926,2,42,2,2,1))
osModLteApnDevEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:osModLteApnDevEntry.setStatus(_A)
_OsModLteApnDevName_Type=EntityName
_OsModLteApnDevName_Object=MibTableColumn
osModLteApnDevName=_OsModLteApnDevName_Object((1,3,6,1,4,1,6926,2,42,2,2,1,2),_OsModLteApnDevName_Type())
osModLteApnDevName.setMaxAccess(_H)
if mibBuilder.loadTexts:osModLteApnDevName.setStatus(_A)
class _OsModLteApnDevPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_OsModLteApnDevPriority_Type.__name__=_E
_OsModLteApnDevPriority_Object=MibTableColumn
osModLteApnDevPriority=_OsModLteApnDevPriority_Object((1,3,6,1,4,1,6926,2,42,2,2,1,3),_OsModLteApnDevPriority_Type())
osModLteApnDevPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:osModLteApnDevPriority.setStatus(_A)
class _OsModLteApnDevID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,63))
_OsModLteApnDevID_Type.__name__=_G
_OsModLteApnDevID_Object=MibTableColumn
osModLteApnDevID=_OsModLteApnDevID_Object((1,3,6,1,4,1,6926,2,42,2,2,1,4),_OsModLteApnDevID_Type())
osModLteApnDevID.setMaxAccess(_D)
if mibBuilder.loadTexts:osModLteApnDevID.setStatus(_A)
class _OsModLteApnDevProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3)))
_OsModLteApnDevProtocol_Type.__name__=_F
_OsModLteApnDevProtocol_Object=MibTableColumn
osModLteApnDevProtocol=_OsModLteApnDevProtocol_Object((1,3,6,1,4,1,6926,2,42,2,2,1,5),_OsModLteApnDevProtocol_Type())
osModLteApnDevProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:osModLteApnDevProtocol.setStatus(_A)
class _OsModLteApnDevBand_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_OsModLteApnDevBand_Type.__name__=_E
_OsModLteApnDevBand_Object=MibTableColumn
osModLteApnDevBand=_OsModLteApnDevBand_Object((1,3,6,1,4,1,6926,2,42,2,2,1,6),_OsModLteApnDevBand_Type())
osModLteApnDevBand.setMaxAccess(_D)
if mibBuilder.loadTexts:osModLteApnDevBand.setStatus(_A)
_OsModLteApnDevDefault_Type=TruthValue
_OsModLteApnDevDefault_Object=MibTableColumn
osModLteApnDevDefault=_OsModLteApnDevDefault_Object((1,3,6,1,4,1,6926,2,42,2,2,1,7),_OsModLteApnDevDefault_Type())
osModLteApnDevDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:osModLteApnDevDefault.setStatus(_A)
_OsModLteApnDevAdminStatus_Type=EntryValidator
_OsModLteApnDevAdminStatus_Object=MibTableColumn
osModLteApnDevAdminStatus=_OsModLteApnDevAdminStatus_Object((1,3,6,1,4,1,6926,2,42,2,2,1,98),_OsModLteApnDevAdminStatus_Type())
osModLteApnDevAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osModLteApnDevAdminStatus.setStatus(_A)
_OsModFiveGApnModTable_Object=MibTable
osModFiveGApnModTable=_OsModFiveGApnModTable_Object((1,3,6,1,4,1,6926,2,42,2,3))
if mibBuilder.loadTexts:osModFiveGApnModTable.setStatus(_A)
_OsModFiveGApnModEntry_Object=MibTableRow
osModFiveGApnModEntry=_OsModFiveGApnModEntry_Object((1,3,6,1,4,1,6926,2,42,2,3,1))
osModFiveGApnModEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:osModFiveGApnModEntry.setStatus(_A)
_OsModFiveGApnModName_Type=EntityName
_OsModFiveGApnModName_Object=MibTableColumn
osModFiveGApnModName=_OsModFiveGApnModName_Object((1,3,6,1,4,1,6926,2,42,2,3,1,2),_OsModFiveGApnModName_Type())
osModFiveGApnModName.setMaxAccess(_H)
if mibBuilder.loadTexts:osModFiveGApnModName.setStatus(_A)
class _OsModFiveGApnModPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_OsModFiveGApnModPriority_Type.__name__=_E
_OsModFiveGApnModPriority_Object=MibTableColumn
osModFiveGApnModPriority=_OsModFiveGApnModPriority_Object((1,3,6,1,4,1,6926,2,42,2,3,1,3),_OsModFiveGApnModPriority_Type())
osModFiveGApnModPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:osModFiveGApnModPriority.setStatus(_A)
class _OsModFiveGApnModID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,63))
_OsModFiveGApnModID_Type.__name__=_G
_OsModFiveGApnModID_Object=MibTableColumn
osModFiveGApnModID=_OsModFiveGApnModID_Object((1,3,6,1,4,1,6926,2,42,2,3,1,4),_OsModFiveGApnModID_Type())
osModFiveGApnModID.setMaxAccess(_C)
if mibBuilder.loadTexts:osModFiveGApnModID.setStatus(_A)
class _OsModFiveGApnModProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3)))
_OsModFiveGApnModProtocol_Type.__name__=_F
_OsModFiveGApnModProtocol_Object=MibTableColumn
osModFiveGApnModProtocol=_OsModFiveGApnModProtocol_Object((1,3,6,1,4,1,6926,2,42,2,3,1,5),_OsModFiveGApnModProtocol_Type())
osModFiveGApnModProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:osModFiveGApnModProtocol.setStatus(_A)
class _OsModFiveGApnModBand_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_OsModFiveGApnModBand_Type.__name__=_E
_OsModFiveGApnModBand_Object=MibTableColumn
osModFiveGApnModBand=_OsModFiveGApnModBand_Object((1,3,6,1,4,1,6926,2,42,2,3,1,6),_OsModFiveGApnModBand_Type())
osModFiveGApnModBand.setMaxAccess(_C)
if mibBuilder.loadTexts:osModFiveGApnModBand.setStatus(_A)
_OsModFiveGApnModLastActive_Type=TruthValue
_OsModFiveGApnModLastActive_Object=MibTableColumn
osModFiveGApnModLastActive=_OsModFiveGApnModLastActive_Object((1,3,6,1,4,1,6926,2,42,2,3,1,7),_OsModFiveGApnModLastActive_Type())
osModFiveGApnModLastActive.setMaxAccess(_C)
if mibBuilder.loadTexts:osModFiveGApnModLastActive.setStatus(_A)
_OsModFiveGApnDevTable_Object=MibTable
osModFiveGApnDevTable=_OsModFiveGApnDevTable_Object((1,3,6,1,4,1,6926,2,42,2,4))
if mibBuilder.loadTexts:osModFiveGApnDevTable.setStatus(_A)
_OsModFiveGApnDevEntry_Object=MibTableRow
osModFiveGApnDevEntry=_OsModFiveGApnDevEntry_Object((1,3,6,1,4,1,6926,2,42,2,4,1))
osModFiveGApnDevEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:osModFiveGApnDevEntry.setStatus(_A)
_OsModFiveGApnDevName_Type=EntityName
_OsModFiveGApnDevName_Object=MibTableColumn
osModFiveGApnDevName=_OsModFiveGApnDevName_Object((1,3,6,1,4,1,6926,2,42,2,4,1,2),_OsModFiveGApnDevName_Type())
osModFiveGApnDevName.setMaxAccess(_H)
if mibBuilder.loadTexts:osModFiveGApnDevName.setStatus(_A)
class _OsModFiveGApnDevPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_OsModFiveGApnDevPriority_Type.__name__=_E
_OsModFiveGApnDevPriority_Object=MibTableColumn
osModFiveGApnDevPriority=_OsModFiveGApnDevPriority_Object((1,3,6,1,4,1,6926,2,42,2,4,1,3),_OsModFiveGApnDevPriority_Type())
osModFiveGApnDevPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:osModFiveGApnDevPriority.setStatus(_A)
class _OsModFiveGApnDevID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,63))
_OsModFiveGApnDevID_Type.__name__=_G
_OsModFiveGApnDevID_Object=MibTableColumn
osModFiveGApnDevID=_OsModFiveGApnDevID_Object((1,3,6,1,4,1,6926,2,42,2,4,1,4),_OsModFiveGApnDevID_Type())
osModFiveGApnDevID.setMaxAccess(_D)
if mibBuilder.loadTexts:osModFiveGApnDevID.setStatus(_A)
class _OsModFiveGApnDevProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3)))
_OsModFiveGApnDevProtocol_Type.__name__=_F
_OsModFiveGApnDevProtocol_Object=MibTableColumn
osModFiveGApnDevProtocol=_OsModFiveGApnDevProtocol_Object((1,3,6,1,4,1,6926,2,42,2,4,1,5),_OsModFiveGApnDevProtocol_Type())
osModFiveGApnDevProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:osModFiveGApnDevProtocol.setStatus(_A)
class _OsModFiveGApnDevBand_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_OsModFiveGApnDevBand_Type.__name__=_E
_OsModFiveGApnDevBand_Object=MibTableColumn
osModFiveGApnDevBand=_OsModFiveGApnDevBand_Object((1,3,6,1,4,1,6926,2,42,2,4,1,6),_OsModFiveGApnDevBand_Type())
osModFiveGApnDevBand.setMaxAccess(_D)
if mibBuilder.loadTexts:osModFiveGApnDevBand.setStatus(_A)
_OsModFiveGApnDevDefault_Type=TruthValue
_OsModFiveGApnDevDefault_Object=MibTableColumn
osModFiveGApnDevDefault=_OsModFiveGApnDevDefault_Object((1,3,6,1,4,1,6926,2,42,2,4,1,7),_OsModFiveGApnDevDefault_Type())
osModFiveGApnDevDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:osModFiveGApnDevDefault.setStatus(_A)
_OsModFiveGApnDevAdminStatus_Type=EntryValidator
_OsModFiveGApnDevAdminStatus_Object=MibTableColumn
osModFiveGApnDevAdminStatus=_OsModFiveGApnDevAdminStatus_Object((1,3,6,1,4,1,6926,2,42,2,4,1,98),_OsModFiveGApnDevAdminStatus_Type())
osModFiveGApnDevAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osModFiveGApnDevAdminStatus.setStatus(_A)
_OsMLteConformance_ObjectIdentity=ObjectIdentity
osMLteConformance=_OsMLteConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,42,100))
_OsMLteMIBCompliances_ObjectIdentity=ObjectIdentity
osMLteMIBCompliances=_OsMLteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,42,100,1))
_OsMLteMIBGroups_ObjectIdentity=ObjectIdentity
osMLteMIBGroups=_OsMLteMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,42,100,2))
osModuleLteGroup=ObjectGroup((1,3,6,1,4,1,6926,2,42,100,2,1))
osModuleLteGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:osModuleLteGroup.setStatus(_A)
osModuleLteOptGroup=ObjectGroup((1,3,6,1,4,1,6926,2,42,100,2,2))
osModuleLteOptGroup.setObjects(*((_B,_M),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:osModuleLteOptGroup.setStatus(_A)
osModLteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,42,100,1,1))
osModLteMIBCompliance.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:osModLteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osModuleLte':osModuleLte,'osModuleLteGen':osModuleLteGen,_M:osModuleLteSupport,'osModuleLteTables':osModuleLteTables,'osModLteApnModTable':osModLteApnModTable,'osModLteApnModEntry':osModLteApnModEntry,_N:osModLteApnModName,_R:osModLteApnModPriority,_S:osModLteApnModID,_T:osModLteApnModProtocol,_U:osModLteApnModBand,_V:osModLteApnModLastActive,'osModLteApnDevTable':osModLteApnDevTable,'osModLteApnDevEntry':osModLteApnDevEntry,_O:osModLteApnDevName,_W:osModLteApnDevPriority,_X:osModLteApnDevID,_Y:osModLteApnDevProtocol,_Z:osModLteApnDevBand,_a:osModLteApnDevDefault,_b:osModLteApnDevAdminStatus,'osModFiveGApnModTable':osModFiveGApnModTable,'osModFiveGApnModEntry':osModFiveGApnModEntry,_P:osModFiveGApnModName,_c:osModFiveGApnModPriority,_d:osModFiveGApnModID,_e:osModFiveGApnModProtocol,_f:osModFiveGApnModBand,_g:osModFiveGApnModLastActive,'osModFiveGApnDevTable':osModFiveGApnDevTable,'osModFiveGApnDevEntry':osModFiveGApnDevEntry,_Q:osModFiveGApnDevName,_h:osModFiveGApnDevPriority,_i:osModFiveGApnDevID,_j:osModFiveGApnDevProtocol,_k:osModFiveGApnDevBand,_l:osModFiveGApnDevDefault,_m:osModFiveGApnDevAdminStatus,'osMLteConformance':osMLteConformance,'osMLteMIBCompliances':osMLteMIBCompliances,'osModLteMIBCompliance':osModLteMIBCompliance,'osMLteMIBGroups':osMLteMIBGroups,_n:osModuleLteGroup,_o:osModuleLteOptGroup})