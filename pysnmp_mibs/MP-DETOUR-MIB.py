_S='mpDetourID'
_R='MP-DETOUR-MIB'
_Q='DisplayString'
_P='NotificationType'
_O='mplspp'
_N='vlantrap'
_M='frpp'
_L='ppp'
_K='trunk'
_J='outband'
_I='lis'
_H='vlan'
_G='atmpp'
_F='read-write'
_E='down'
_D='up'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_P,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_P,'TimeTicks','Unsigned32','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Q,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_NecProduct_ObjectIdentity=ObjectIdentity
necProduct=_NecProduct_ObjectIdentity((1,3,6,1,4,1,119,1))
_Datax_ObjectIdentity=ObjectIdentity
datax=_Datax_ObjectIdentity((1,3,6,1,4,1,119,1,3))
_Mmpf_ObjectIdentity=ObjectIdentity
mmpf=_Mmpf_ObjectIdentity((1,3,6,1,4,1,119,1,3,13))
_Mmn9110_ObjectIdentity=ObjectIdentity
mmn9110=_Mmn9110_ObjectIdentity((1,3,6,1,4,1,119,1,3,13,1))
_Mmn9120_ObjectIdentity=ObjectIdentity
mmn9120=_Mmn9120_ObjectIdentity((1,3,6,1,4,1,119,1,3,13,2))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_Datax_mib_ObjectIdentity=ObjectIdentity
datax_mib=_Datax_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,3))
_Mmpf_mib_ObjectIdentity=ObjectIdentity
mmpf_mib=_Mmpf_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13))
_MpDetour_ObjectIdentity=ObjectIdentity
mpDetour=_MpDetour_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,130))
_MpDetourTable_Object=MibTable
mpDetourTable=_MpDetourTable_Object((1,3,6,1,4,1,119,2,3,3,13,130,1))
if mibBuilder.loadTexts:mpDetourTable.setStatus(_A)
_MpDetourEntry_Object=MibTableRow
mpDetourEntry=_MpDetourEntry_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1))
mpDetourEntry.setIndexNames((0,_R,_S))
if mibBuilder.loadTexts:mpDetourEntry.setStatus(_A)
_MpDetourID_Type=Integer32
_MpDetourID_Object=MibTableColumn
mpDetourID=_MpDetourID_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,1),_MpDetourID_Type())
mpDetourID.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDetourID.setStatus(_A)
_MpObservationIfindex_Type=Integer32
_MpObservationIfindex_Object=MibTableColumn
mpObservationIfindex=_MpObservationIfindex_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,2),_MpObservationIfindex_Type())
mpObservationIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpObservationIfindex.setStatus(_A)
class _MpObservationIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9)))
_MpObservationIfType_Type.__name__=_C
_MpObservationIfType_Object=MibTableColumn
mpObservationIfType=_MpObservationIfType_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,3),_MpObservationIfType_Type())
mpObservationIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpObservationIfType.setStatus(_A)
_MpObservationIfNumber_Type=Integer32
_MpObservationIfNumber_Object=MibTableColumn
mpObservationIfNumber=_MpObservationIfNumber_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,4),_MpObservationIfNumber_Type())
mpObservationIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpObservationIfNumber.setStatus(_A)
_MpDetourIfindex_Type=Integer32
_MpDetourIfindex_Object=MibTableColumn
mpDetourIfindex=_MpDetourIfindex_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,5),_MpDetourIfindex_Type())
mpDetourIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDetourIfindex.setStatus(_A)
class _MpDetourIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9)))
_MpDetourIfType_Type.__name__=_C
_MpDetourIfType_Object=MibTableColumn
mpDetourIfType=_MpDetourIfType_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,6),_MpDetourIfType_Type())
mpDetourIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDetourIfType.setStatus(_A)
_MpDetourIfNumber_Type=Integer32
_MpDetourIfNumber_Object=MibTableColumn
mpDetourIfNumber=_MpDetourIfNumber_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,7),_MpDetourIfNumber_Type())
mpDetourIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDetourIfNumber.setStatus(_A)
class _MpObservationAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MpObservationAdminStatus_Type.__name__=_C
_MpObservationAdminStatus_Object=MibTableColumn
mpObservationAdminStatus=_MpObservationAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,8),_MpObservationAdminStatus_Type())
mpObservationAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:mpObservationAdminStatus.setStatus(_A)
class _MpObservationOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MpObservationOperStatus_Type.__name__=_C
_MpObservationOperStatus_Object=MibTableColumn
mpObservationOperStatus=_MpObservationOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,9),_MpObservationOperStatus_Type())
mpObservationOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpObservationOperStatus.setStatus(_A)
_MpDiscardIfindex_Type=Integer32
_MpDiscardIfindex_Object=MibTableColumn
mpDiscardIfindex=_MpDiscardIfindex_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,10),_MpDiscardIfindex_Type())
mpDiscardIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDiscardIfindex.setStatus(_A)
class _MpDiscardIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9)))
_MpDiscardIfType_Type.__name__=_C
_MpDiscardIfType_Object=MibTableColumn
mpDiscardIfType=_MpDiscardIfType_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,11),_MpDiscardIfType_Type())
mpDiscardIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDiscardIfType.setStatus(_A)
_MpDiscardIfNumber_Type=Integer32
_MpDiscardIfNumber_Object=MibTableColumn
mpDiscardIfNumber=_MpDiscardIfNumber_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,12),_MpDiscardIfNumber_Type())
mpDiscardIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDiscardIfNumber.setStatus(_A)
class _MpDetourAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MpDetourAdminStatus_Type.__name__=_C
_MpDetourAdminStatus_Object=MibTableColumn
mpDetourAdminStatus=_MpDetourAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,13),_MpDetourAdminStatus_Type())
mpDetourAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:mpDetourAdminStatus.setStatus(_A)
class _MpDetourOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MpDetourOperStatus_Type.__name__=_C
_MpDetourOperStatus_Object=MibTableColumn
mpDetourOperStatus=_MpDetourOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,14),_MpDetourOperStatus_Type())
mpDetourOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDetourOperStatus.setStatus(_A)
class _MpDiscardAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MpDiscardAdminStatus_Type.__name__=_C
_MpDiscardAdminStatus_Object=MibTableColumn
mpDiscardAdminStatus=_MpDiscardAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,15),_MpDiscardAdminStatus_Type())
mpDiscardAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:mpDiscardAdminStatus.setStatus(_A)
class _MpDiscardOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MpDiscardOperStatus_Type.__name__=_C
_MpDiscardOperStatus_Object=MibTableColumn
mpDiscardOperStatus=_MpDiscardOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,16),_MpDiscardOperStatus_Type())
mpDiscardOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDiscardOperStatus.setStatus(_A)
class _MpRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MpRouteStatus_Type.__name__=_C
_MpRouteStatus_Object=MibTableColumn
mpRouteStatus=_MpRouteStatus_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,17),_MpRouteStatus_Type())
mpRouteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpRouteStatus.setStatus(_A)
class _MpInhibitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_MpInhibitMode_Type.__name__=_C
_MpInhibitMode_Object=MibTableColumn
mpInhibitMode=_MpInhibitMode_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,18),_MpInhibitMode_Type())
mpInhibitMode.setMaxAccess(_F)
if mibBuilder.loadTexts:mpInhibitMode.setStatus(_A)
class _MpWatchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_MpWatchMode_Type.__name__=_C
_MpWatchMode_Object=MibTableColumn
mpWatchMode=_MpWatchMode_Object((1,3,6,1,4,1,119,2,3,3,13,130,1,1,19),_MpWatchMode_Type())
mpWatchMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWatchMode.setStatus(_A)
_MpDetourConfigChangeTimeStamp_ObjectIdentity=ObjectIdentity
mpDetourConfigChangeTimeStamp=_MpDetourConfigChangeTimeStamp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,130,2))
_MpDetourConfigLastChange_Type=TimeTicks
_MpDetourConfigLastChange_Object=MibScalar
mpDetourConfigLastChange=_MpDetourConfigLastChange_Object((1,3,6,1,4,1,119,2,3,3,13,130,2,1),_MpDetourConfigLastChange_Type())
mpDetourConfigLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDetourConfigLastChange.setStatus(_A)
_MpDetourStatusTimeStamp_ObjectIdentity=ObjectIdentity
mpDetourStatusTimeStamp=_MpDetourStatusTimeStamp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,130,3))
_MpDetourStatusLastChange_Type=TimeTicks
_MpDetourStatusLastChange_Object=MibScalar
mpDetourStatusLastChange=_MpDetourStatusLastChange_Object((1,3,6,1,4,1,119,2,3,3,13,130,3,1),_MpDetourStatusLastChange_Type())
mpDetourStatusLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:mpDetourStatusLastChange.setStatus(_A)
mibBuilder.exportSymbols(_R,**{_Q:DisplayString,'org':org,'dod':dod,'internet':internet,'private':private,'enterprises':enterprises,'nec':nec,'necProduct':necProduct,'datax':datax,'mmpf':mmpf,'mmn9110':mmn9110,'mmn9120':mmn9120,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'datax-mib':datax_mib,'mmpf-mib':mmpf_mib,'mpDetour':mpDetour,'mpDetourTable':mpDetourTable,'mpDetourEntry':mpDetourEntry,_S:mpDetourID,'mpObservationIfindex':mpObservationIfindex,'mpObservationIfType':mpObservationIfType,'mpObservationIfNumber':mpObservationIfNumber,'mpDetourIfindex':mpDetourIfindex,'mpDetourIfType':mpDetourIfType,'mpDetourIfNumber':mpDetourIfNumber,'mpObservationAdminStatus':mpObservationAdminStatus,'mpObservationOperStatus':mpObservationOperStatus,'mpDiscardIfindex':mpDiscardIfindex,'mpDiscardIfType':mpDiscardIfType,'mpDiscardIfNumber':mpDiscardIfNumber,'mpDetourAdminStatus':mpDetourAdminStatus,'mpDetourOperStatus':mpDetourOperStatus,'mpDiscardAdminStatus':mpDiscardAdminStatus,'mpDiscardOperStatus':mpDiscardOperStatus,'mpRouteStatus':mpRouteStatus,'mpInhibitMode':mpInhibitMode,'mpWatchMode':mpWatchMode,'mpDetourConfigChangeTimeStamp':mpDetourConfigChangeTimeStamp,'mpDetourConfigLastChange':mpDetourConfigLastChange,'mpDetourStatusTimeStamp':mpDetourStatusTimeStamp,'mpDetourStatusLastChange':mpDetourStatusLastChange})