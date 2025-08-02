_L='sfpsAgentBinderyConfigHashIndex'
_K='sfpsAgentBinderyConfigHashLeaf'
_J='read-write'
_I='unset'
_H='CTRON-SFPS-BINDERY-MIB'
_G='invalid'
_F='other'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsAgentConfig,=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsAgentConfig')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
_SfpsAgentBinderyConfigTable_Object=MibTable
sfpsAgentBinderyConfigTable=_SfpsAgentBinderyConfigTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1))
if mibBuilder.loadTexts:sfpsAgentBinderyConfigTable.setStatus(_A)
_SfpsAgentBinderyConfigEntry_Object=MibTableRow
sfpsAgentBinderyConfigEntry=_SfpsAgentBinderyConfigEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1))
sfpsAgentBinderyConfigEntry.setIndexNames((0,_H,_K),(0,_H,_L))
if mibBuilder.loadTexts:sfpsAgentBinderyConfigEntry.setStatus(_A)
_SfpsAgentBinderyConfigHashLeaf_Type=HexInteger
_SfpsAgentBinderyConfigHashLeaf_Object=MibTableColumn
sfpsAgentBinderyConfigHashLeaf=_SfpsAgentBinderyConfigHashLeaf_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,1),_SfpsAgentBinderyConfigHashLeaf_Type())
sfpsAgentBinderyConfigHashLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigHashLeaf.setStatus(_A)
_SfpsAgentBinderyConfigHashIndex_Type=Integer32
_SfpsAgentBinderyConfigHashIndex_Object=MibTableColumn
sfpsAgentBinderyConfigHashIndex=_SfpsAgentBinderyConfigHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,2),_SfpsAgentBinderyConfigHashIndex_Type())
sfpsAgentBinderyConfigHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigHashIndex.setStatus(_A)
_SfpsAgentBinderyConfigName_Type=DisplayString
_SfpsAgentBinderyConfigName_Object=MibTableColumn
sfpsAgentBinderyConfigName=_SfpsAgentBinderyConfigName_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,3),_SfpsAgentBinderyConfigName_Type())
sfpsAgentBinderyConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigName.setStatus(_A)
_SfpsAgentBinderyConfigType_Type=DisplayString
_SfpsAgentBinderyConfigType_Object=MibTableColumn
sfpsAgentBinderyConfigType=_SfpsAgentBinderyConfigType_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,4),_SfpsAgentBinderyConfigType_Type())
sfpsAgentBinderyConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigType.setStatus(_A)
class _SfpsAgentBinderyConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kStatusRunning',1),('kStatusHalted',2),('kStatusPending',3),('kStatusFaulted',4),('kStatusNotStarted',5)))
_SfpsAgentBinderyConfigOperStatus_Type.__name__=_C
_SfpsAgentBinderyConfigOperStatus_Object=MibTableColumn
sfpsAgentBinderyConfigOperStatus=_SfpsAgentBinderyConfigOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,5),_SfpsAgentBinderyConfigOperStatus_Type())
sfpsAgentBinderyConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigOperStatus.setStatus(_A)
class _SfpsAgentBinderyConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_D,2),(_E,3)))
_SfpsAgentBinderyConfigAdminStatus_Type.__name__=_C
_SfpsAgentBinderyConfigAdminStatus_Object=MibTableColumn
sfpsAgentBinderyConfigAdminStatus=_SfpsAgentBinderyConfigAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,6),_SfpsAgentBinderyConfigAdminStatus_Type())
sfpsAgentBinderyConfigAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigAdminStatus.setStatus(_A)
_SfpsAgentBinderyConfigStatusTime_Type=TimeTicks
_SfpsAgentBinderyConfigStatusTime_Object=MibTableColumn
sfpsAgentBinderyConfigStatusTime=_SfpsAgentBinderyConfigStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,7),_SfpsAgentBinderyConfigStatusTime_Type())
sfpsAgentBinderyConfigStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigStatusTime.setStatus(_A)
class _SfpsAgentBinderyConfigNVStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_D,2),(_E,3),(_I,4)))
_SfpsAgentBinderyConfigNVStatus_Type.__name__=_C
_SfpsAgentBinderyConfigNVStatus_Object=MibTableColumn
sfpsAgentBinderyConfigNVStatus=_SfpsAgentBinderyConfigNVStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,1,1,8),_SfpsAgentBinderyConfigNVStatus_Type())
sfpsAgentBinderyConfigNVStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:sfpsAgentBinderyConfigNVStatus.setStatus(_A)
_SfpsAgentBinderyAPI_ObjectIdentity=ObjectIdentity
sfpsAgentBinderyAPI=_SfpsAgentBinderyAPI_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,2,7,2))
class _SfpsAgentBinderyAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('getStatus',1),('nextElem',2),(_D,3),('disableInNvram',4),(_E,5),('enableInNvram',6),('clear',7),('clearAll',8)))
_SfpsAgentBinderyAPIVerb_Type.__name__=_C
_SfpsAgentBinderyAPIVerb_Object=MibScalar
sfpsAgentBinderyAPIVerb=_SfpsAgentBinderyAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,1),_SfpsAgentBinderyAPIVerb_Type())
sfpsAgentBinderyAPIVerb.setMaxAccess(_J)
if mibBuilder.loadTexts:sfpsAgentBinderyAPIVerb.setStatus(_A)
_SfpsAgentBinderyAPIElementName_Type=DisplayString
_SfpsAgentBinderyAPIElementName_Object=MibScalar
sfpsAgentBinderyAPIElementName=_SfpsAgentBinderyAPIElementName_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,2),_SfpsAgentBinderyAPIElementName_Type())
sfpsAgentBinderyAPIElementName.setMaxAccess(_J)
if mibBuilder.loadTexts:sfpsAgentBinderyAPIElementName.setStatus(_A)
class _SfpsAgentBinderyAPINVStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_D,2),(_E,3),(_I,4),(_G,5)))
_SfpsAgentBinderyAPINVStatus_Type.__name__=_C
_SfpsAgentBinderyAPINVStatus_Object=MibScalar
sfpsAgentBinderyAPINVStatus=_SfpsAgentBinderyAPINVStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,3),_SfpsAgentBinderyAPINVStatus_Type())
sfpsAgentBinderyAPINVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyAPINVStatus.setStatus(_A)
class _SfpsAgentBinderyAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_D,2),(_E,3),(_G,4)))
_SfpsAgentBinderyAPIAdminStatus_Type.__name__=_C
_SfpsAgentBinderyAPIAdminStatus_Object=MibScalar
sfpsAgentBinderyAPIAdminStatus=_SfpsAgentBinderyAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,4),_SfpsAgentBinderyAPIAdminStatus_Type())
sfpsAgentBinderyAPIAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyAPIAdminStatus.setStatus(_A)
class _SfpsAgentBinderyAPIOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('running',1),('halted',2),('pending',3),('faulted',4),('notStarted',5),(_G,6)))
_SfpsAgentBinderyAPIOperStatus_Type.__name__=_C
_SfpsAgentBinderyAPIOperStatus_Object=MibScalar
sfpsAgentBinderyAPIOperStatus=_SfpsAgentBinderyAPIOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,5),_SfpsAgentBinderyAPIOperStatus_Type())
sfpsAgentBinderyAPIOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyAPIOperStatus.setStatus(_A)
_SfpsAgentBinderyAPINvSet_Type=Integer32
_SfpsAgentBinderyAPINvSet_Object=MibScalar
sfpsAgentBinderyAPINvSet=_SfpsAgentBinderyAPINvSet_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,6),_SfpsAgentBinderyAPINvSet_Type())
sfpsAgentBinderyAPINvSet.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyAPINvSet.setStatus(_A)
_SfpsAgentBinderyAPINvTotal_Type=Integer32
_SfpsAgentBinderyAPINvTotal_Object=MibScalar
sfpsAgentBinderyAPINvTotal=_SfpsAgentBinderyAPINvTotal_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,7),_SfpsAgentBinderyAPINvTotal_Type())
sfpsAgentBinderyAPINvTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyAPINvTotal.setStatus(_A)
class _SfpsAgentBinderyAPIDefaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_D,2),(_E,3),(_I,4),(_G,5)))
_SfpsAgentBinderyAPIDefaultStatus_Type.__name__=_C
_SfpsAgentBinderyAPIDefaultStatus_Object=MibScalar
sfpsAgentBinderyAPIDefaultStatus=_SfpsAgentBinderyAPIDefaultStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,7,2,8),_SfpsAgentBinderyAPIDefaultStatus_Type())
sfpsAgentBinderyAPIDefaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAgentBinderyAPIDefaultStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'HexInteger':HexInteger,'sfpsAgentBinderyConfigTable':sfpsAgentBinderyConfigTable,'sfpsAgentBinderyConfigEntry':sfpsAgentBinderyConfigEntry,_K:sfpsAgentBinderyConfigHashLeaf,_L:sfpsAgentBinderyConfigHashIndex,'sfpsAgentBinderyConfigName':sfpsAgentBinderyConfigName,'sfpsAgentBinderyConfigType':sfpsAgentBinderyConfigType,'sfpsAgentBinderyConfigOperStatus':sfpsAgentBinderyConfigOperStatus,'sfpsAgentBinderyConfigAdminStatus':sfpsAgentBinderyConfigAdminStatus,'sfpsAgentBinderyConfigStatusTime':sfpsAgentBinderyConfigStatusTime,'sfpsAgentBinderyConfigNVStatus':sfpsAgentBinderyConfigNVStatus,'sfpsAgentBinderyAPI':sfpsAgentBinderyAPI,'sfpsAgentBinderyAPIVerb':sfpsAgentBinderyAPIVerb,'sfpsAgentBinderyAPIElementName':sfpsAgentBinderyAPIElementName,'sfpsAgentBinderyAPINVStatus':sfpsAgentBinderyAPINVStatus,'sfpsAgentBinderyAPIAdminStatus':sfpsAgentBinderyAPIAdminStatus,'sfpsAgentBinderyAPIOperStatus':sfpsAgentBinderyAPIOperStatus,'sfpsAgentBinderyAPINvSet':sfpsAgentBinderyAPINvSet,'sfpsAgentBinderyAPINvTotal':sfpsAgentBinderyAPINvTotal,'sfpsAgentBinderyAPIDefaultStatus':sfpsAgentBinderyAPIDefaultStatus})