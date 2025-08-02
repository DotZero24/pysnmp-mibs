_V='rbnMemoryGroup'
_U='rbnSmsMemoryGroup'
_T='rbnMemoryCumulBlocks'
_S='rbnMemoryBlocksInUse'
_R='rbnMemoryKBytesInUse'
_Q='rbnMemoryFreeKBytes'
_P='rbnMemoryModule'
_O='rbnSmsMemoryCumulBlocks'
_N='rbnSmsMemoryBlocksInUse'
_M='rbnSmsMemoryBytesInUse'
_L='rbnSmsMemoryFreeBytes'
_K='rbnSmsMemoryModule'
_J='KBytes'
_I='rbnMemoryIndex'
_H='not-accessible'
_G='rbnSmsMemoryIndex'
_F='SnmpAdminString'
_E='Unsigned32'
_D='current'
_C='read-only'
_B='obsolete'
_A='RBN-MEMORY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnKBytes,=mibBuilder.importSymbols('RBN-TC','RbnKBytes')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnMemoryMib=ModuleIdentity((1,3,6,1,4,1,2352,2,16))
if mibBuilder.loadTexts:rbnMemoryMib.setRevisions(('2004-03-05 17:00','2002-06-26 00:00','2002-01-03 17:00'))
_RbnMemoryMIBNotifications_ObjectIdentity=ObjectIdentity
rbnMemoryMIBNotifications=_RbnMemoryMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,16,0))
_RbnMemoryMIBObjects_ObjectIdentity=ObjectIdentity
rbnMemoryMIBObjects=_RbnMemoryMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,16,1))
_RbnSmsMemoryTable_Object=MibTable
rbnSmsMemoryTable=_RbnSmsMemoryTable_Object((1,3,6,1,4,1,2352,2,16,1,1))
if mibBuilder.loadTexts:rbnSmsMemoryTable.setStatus(_B)
_RbnSmsMemoryEntry_Object=MibTableRow
rbnSmsMemoryEntry=_RbnSmsMemoryEntry_Object((1,3,6,1,4,1,2352,2,16,1,1,1))
rbnSmsMemoryEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:rbnSmsMemoryEntry.setStatus(_B)
class _RbnSmsMemoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RbnSmsMemoryIndex_Type.__name__=_E
_RbnSmsMemoryIndex_Object=MibTableColumn
rbnSmsMemoryIndex=_RbnSmsMemoryIndex_Object((1,3,6,1,4,1,2352,2,16,1,1,1,1),_RbnSmsMemoryIndex_Type())
rbnSmsMemoryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rbnSmsMemoryIndex.setStatus(_B)
class _RbnSmsMemoryModule_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbnSmsMemoryModule_Type.__name__=_F
_RbnSmsMemoryModule_Object=MibTableColumn
rbnSmsMemoryModule=_RbnSmsMemoryModule_Object((1,3,6,1,4,1,2352,2,16,1,1,1,2),_RbnSmsMemoryModule_Type())
rbnSmsMemoryModule.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSmsMemoryModule.setStatus(_B)
class _RbnSmsMemoryFreeBytes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RbnSmsMemoryFreeBytes_Type.__name__=_E
_RbnSmsMemoryFreeBytes_Object=MibTableColumn
rbnSmsMemoryFreeBytes=_RbnSmsMemoryFreeBytes_Object((1,3,6,1,4,1,2352,2,16,1,1,1,3),_RbnSmsMemoryFreeBytes_Type())
rbnSmsMemoryFreeBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSmsMemoryFreeBytes.setStatus(_B)
class _RbnSmsMemoryBytesInUse_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RbnSmsMemoryBytesInUse_Type.__name__=_E
_RbnSmsMemoryBytesInUse_Object=MibTableColumn
rbnSmsMemoryBytesInUse=_RbnSmsMemoryBytesInUse_Object((1,3,6,1,4,1,2352,2,16,1,1,1,4),_RbnSmsMemoryBytesInUse_Type())
rbnSmsMemoryBytesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSmsMemoryBytesInUse.setStatus(_B)
class _RbnSmsMemoryBlocksInUse_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RbnSmsMemoryBlocksInUse_Type.__name__=_E
_RbnSmsMemoryBlocksInUse_Object=MibTableColumn
rbnSmsMemoryBlocksInUse=_RbnSmsMemoryBlocksInUse_Object((1,3,6,1,4,1,2352,2,16,1,1,1,5),_RbnSmsMemoryBlocksInUse_Type())
rbnSmsMemoryBlocksInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSmsMemoryBlocksInUse.setStatus(_B)
class _RbnSmsMemoryCumulBlocks_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RbnSmsMemoryCumulBlocks_Type.__name__=_E
_RbnSmsMemoryCumulBlocks_Object=MibTableColumn
rbnSmsMemoryCumulBlocks=_RbnSmsMemoryCumulBlocks_Object((1,3,6,1,4,1,2352,2,16,1,1,1,6),_RbnSmsMemoryCumulBlocks_Type())
rbnSmsMemoryCumulBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnSmsMemoryCumulBlocks.setStatus(_B)
_RbnMemoryTable_Object=MibTable
rbnMemoryTable=_RbnMemoryTable_Object((1,3,6,1,4,1,2352,2,16,1,2))
if mibBuilder.loadTexts:rbnMemoryTable.setStatus(_D)
_RbnMemoryEntry_Object=MibTableRow
rbnMemoryEntry=_RbnMemoryEntry_Object((1,3,6,1,4,1,2352,2,16,1,2,1))
rbnMemoryEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:rbnMemoryEntry.setStatus(_D)
class _RbnMemoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RbnMemoryIndex_Type.__name__=_E
_RbnMemoryIndex_Object=MibTableColumn
rbnMemoryIndex=_RbnMemoryIndex_Object((1,3,6,1,4,1,2352,2,16,1,2,1,1),_RbnMemoryIndex_Type())
rbnMemoryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rbnMemoryIndex.setStatus(_D)
class _RbnMemoryModule_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbnMemoryModule_Type.__name__=_F
_RbnMemoryModule_Object=MibTableColumn
rbnMemoryModule=_RbnMemoryModule_Object((1,3,6,1,4,1,2352,2,16,1,2,1,2),_RbnMemoryModule_Type())
rbnMemoryModule.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMemoryModule.setStatus(_D)
_RbnMemoryFreeKBytes_Type=RbnKBytes
_RbnMemoryFreeKBytes_Object=MibTableColumn
rbnMemoryFreeKBytes=_RbnMemoryFreeKBytes_Object((1,3,6,1,4,1,2352,2,16,1,2,1,3),_RbnMemoryFreeKBytes_Type())
rbnMemoryFreeKBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMemoryFreeKBytes.setStatus(_D)
if mibBuilder.loadTexts:rbnMemoryFreeKBytes.setUnits(_J)
_RbnMemoryKBytesInUse_Type=RbnKBytes
_RbnMemoryKBytesInUse_Object=MibTableColumn
rbnMemoryKBytesInUse=_RbnMemoryKBytesInUse_Object((1,3,6,1,4,1,2352,2,16,1,2,1,4),_RbnMemoryKBytesInUse_Type())
rbnMemoryKBytesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMemoryKBytesInUse.setStatus(_D)
if mibBuilder.loadTexts:rbnMemoryKBytesInUse.setUnits(_J)
class _RbnMemoryBlocksInUse_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RbnMemoryBlocksInUse_Type.__name__=_E
_RbnMemoryBlocksInUse_Object=MibTableColumn
rbnMemoryBlocksInUse=_RbnMemoryBlocksInUse_Object((1,3,6,1,4,1,2352,2,16,1,2,1,5),_RbnMemoryBlocksInUse_Type())
rbnMemoryBlocksInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMemoryBlocksInUse.setStatus(_D)
class _RbnMemoryCumulBlocks_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RbnMemoryCumulBlocks_Type.__name__=_E
_RbnMemoryCumulBlocks_Object=MibTableColumn
rbnMemoryCumulBlocks=_RbnMemoryCumulBlocks_Object((1,3,6,1,4,1,2352,2,16,1,2,1,6),_RbnMemoryCumulBlocks_Type())
rbnMemoryCumulBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMemoryCumulBlocks.setStatus(_D)
_RbnMemoryMIBConformance_ObjectIdentity=ObjectIdentity
rbnMemoryMIBConformance=_RbnMemoryMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,16,2))
_RbnSmsMemoryCompliances_ObjectIdentity=ObjectIdentity
rbnSmsMemoryCompliances=_RbnSmsMemoryCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,16,2,1))
_RbnSmsMemoryGroups_ObjectIdentity=ObjectIdentity
rbnSmsMemoryGroups=_RbnSmsMemoryGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,16,2,2))
_RbnMemoryCompliances_ObjectIdentity=ObjectIdentity
rbnMemoryCompliances=_RbnMemoryCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,16,2,3))
_RbnMemoryGroups_ObjectIdentity=ObjectIdentity
rbnMemoryGroups=_RbnMemoryGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,16,2,4))
rbnSmsMemoryGroup=ObjectGroup((1,3,6,1,4,1,2352,2,16,2,2,1))
rbnSmsMemoryGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:rbnSmsMemoryGroup.setStatus(_B)
rbnMemoryGroup=ObjectGroup((1,3,6,1,4,1,2352,2,16,2,4,1))
rbnMemoryGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:rbnMemoryGroup.setStatus(_D)
rbnSmsMemoryCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,16,2,1,1))
rbnSmsMemoryCompliance.setObjects((_A,_U))
if mibBuilder.loadTexts:rbnSmsMemoryCompliance.setStatus(_B)
rbnMemoryCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,16,2,3,1))
rbnMemoryCompliance.setObjects((_A,_V))
if mibBuilder.loadTexts:rbnMemoryCompliance.setStatus(_D)
mibBuilder.exportSymbols(_A,**{'rbnMemoryMib':rbnMemoryMib,'rbnMemoryMIBNotifications':rbnMemoryMIBNotifications,'rbnMemoryMIBObjects':rbnMemoryMIBObjects,'rbnSmsMemoryTable':rbnSmsMemoryTable,'rbnSmsMemoryEntry':rbnSmsMemoryEntry,_G:rbnSmsMemoryIndex,_K:rbnSmsMemoryModule,_L:rbnSmsMemoryFreeBytes,_M:rbnSmsMemoryBytesInUse,_N:rbnSmsMemoryBlocksInUse,_O:rbnSmsMemoryCumulBlocks,'rbnMemoryTable':rbnMemoryTable,'rbnMemoryEntry':rbnMemoryEntry,_I:rbnMemoryIndex,_P:rbnMemoryModule,_Q:rbnMemoryFreeKBytes,_R:rbnMemoryKBytesInUse,_S:rbnMemoryBlocksInUse,_T:rbnMemoryCumulBlocks,'rbnMemoryMIBConformance':rbnMemoryMIBConformance,'rbnSmsMemoryCompliances':rbnSmsMemoryCompliances,'rbnSmsMemoryCompliance':rbnSmsMemoryCompliance,'rbnSmsMemoryGroups':rbnSmsMemoryGroups,_U:rbnSmsMemoryGroup,'rbnMemoryCompliances':rbnMemoryCompliances,'rbnMemoryCompliance':rbnMemoryCompliance,'rbnMemoryGroups':rbnMemoryGroups,_V:rbnMemoryGroup})