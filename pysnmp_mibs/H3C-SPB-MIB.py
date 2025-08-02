_P='h3cSpbConflictBMac'
_O='h3cSpbConflictSPSourceID'
_N='not-accessible'
_M='h3cSpbSrvTableEntryIsid'
_L='h3cSpbSrvTableEntryTopIx'
_K='Unsigned32'
_J='ifIndex'
_I='IF-MIB'
_H='h3cSpbConflictSysID'
_G='accessible-for-notify'
_F='disabled'
_E='enabled'
_D='read-write'
_C='Integer32'
_B='H3C-SPB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
IEEE8021SpbmSPsourceId,=mibBuilder.importSymbols('IEEE8021-SPB-MIB','IEEE8021SpbmSPsourceId')
ifIndex,=mibBuilder.importSymbols(_I,_J)
VlanIdOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIdOrNone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
h3cSpb=ModuleIdentity((1,3,6,1,4,1,2011,10,2,128))
if mibBuilder.loadTexts:h3cSpb.setRevisions(('2012-11-22 00:00',))
_H3cSpbObjects_ObjectIdentity=ObjectIdentity
h3cSpbObjects=_H3cSpbObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,128,1))
_H3cSpbSysObjects_ObjectIdentity=ObjectIdentity
h3cSpbSysObjects=_H3cSpbSysObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,128,1,1))
class _H3cSpbSysStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_H3cSpbSysStatus_Type.__name__=_C
_H3cSpbSysStatus_Object=MibScalar
h3cSpbSysStatus=_H3cSpbSysStatus_Object((1,3,6,1,4,1,2011,10,2,128,1,1,1),_H3cSpbSysStatus_Type())
h3cSpbSysStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSpbSysStatus.setStatus(_A)
class _H3cSpbMulticastBVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_H3cSpbMulticastBVlanStatus_Type.__name__=_C
_H3cSpbMulticastBVlanStatus_Object=MibScalar
h3cSpbMulticastBVlanStatus=_H3cSpbMulticastBVlanStatus_Object((1,3,6,1,4,1,2011,10,2,128,1,1,2),_H3cSpbMulticastBVlanStatus_Type())
h3cSpbMulticastBVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSpbMulticastBVlanStatus.setStatus(_A)
_H3cSpbConfig_ObjectIdentity=ObjectIdentity
h3cSpbConfig=_H3cSpbConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,128,1,2))
_H3cSpbIfTable_Object=MibTable
h3cSpbIfTable=_H3cSpbIfTable_Object((1,3,6,1,4,1,2011,10,2,128,1,2,1))
if mibBuilder.loadTexts:h3cSpbIfTable.setStatus(_A)
_H3cSpbIfEntry_Object=MibTableRow
h3cSpbIfEntry=_H3cSpbIfEntry_Object((1,3,6,1,4,1,2011,10,2,128,1,2,1,1))
h3cSpbIfEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cSpbIfEntry.setStatus(_A)
class _H3cSpbIfStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_H3cSpbIfStatus_Type.__name__=_C
_H3cSpbIfStatus_Object=MibTableColumn
h3cSpbIfStatus=_H3cSpbIfStatus_Object((1,3,6,1,4,1,2011,10,2,128,1,2,1,1,1),_H3cSpbIfStatus_Type())
h3cSpbIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSpbIfStatus.setStatus(_A)
_H3cSpbSrvTable_Object=MibTable
h3cSpbSrvTable=_H3cSpbSrvTable_Object((1,3,6,1,4,1,2011,10,2,128,1,2,2))
if mibBuilder.loadTexts:h3cSpbSrvTable.setStatus(_A)
_H3cSpbSrvEntry_Object=MibTableRow
h3cSpbSrvEntry=_H3cSpbSrvEntry_Object((1,3,6,1,4,1,2011,10,2,128,1,2,2,1))
h3cSpbSrvEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:h3cSpbSrvEntry.setStatus(_A)
_H3cSpbSrvTableEntryTopIx_Type=Unsigned32
_H3cSpbSrvTableEntryTopIx_Object=MibTableColumn
h3cSpbSrvTableEntryTopIx=_H3cSpbSrvTableEntryTopIx_Object((1,3,6,1,4,1,2011,10,2,128,1,2,2,1,1),_H3cSpbSrvTableEntryTopIx_Type())
h3cSpbSrvTableEntryTopIx.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cSpbSrvTableEntryTopIx.setStatus(_A)
class _H3cSpbSrvTableEntryIsid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(255,16777215))
_H3cSpbSrvTableEntryIsid_Type.__name__=_K
_H3cSpbSrvTableEntryIsid_Object=MibTableColumn
h3cSpbSrvTableEntryIsid=_H3cSpbSrvTableEntryIsid_Object((1,3,6,1,4,1,2011,10,2,128,1,2,2,1,2),_H3cSpbSrvTableEntryIsid_Type())
h3cSpbSrvTableEntryIsid.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cSpbSrvTableEntryIsid.setStatus(_A)
_H3cSpbSrvTableEntryBaseVid_Type=VlanIdOrNone
_H3cSpbSrvTableEntryBaseVid_Object=MibTableColumn
h3cSpbSrvTableEntryBaseVid=_H3cSpbSrvTableEntryBaseVid_Object((1,3,6,1,4,1,2011,10,2,128,1,2,2,1,3),_H3cSpbSrvTableEntryBaseVid_Type())
h3cSpbSrvTableEntryBaseVid.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSpbSrvTableEntryBaseVid.setStatus(_A)
class _H3cSpbSrvTableEntryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('headEnd',1),('tandem',2)))
_H3cSpbSrvTableEntryMode_Type.__name__=_C
_H3cSpbSrvTableEntryMode_Object=MibTableColumn
h3cSpbSrvTableEntryMode=_H3cSpbSrvTableEntryMode_Object((1,3,6,1,4,1,2011,10,2,128,1,2,2,1,4),_H3cSpbSrvTableEntryMode_Type())
h3cSpbSrvTableEntryMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSpbSrvTableEntryMode.setStatus(_A)
_H3cSpbTrap_ObjectIdentity=ObjectIdentity
h3cSpbTrap=_H3cSpbTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,128,1,3))
_H3cSpbTraps_ObjectIdentity=ObjectIdentity
h3cSpbTraps=_H3cSpbTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,128,1,3,0))
_H3cSpbTrapsObjects_ObjectIdentity=ObjectIdentity
h3cSpbTrapsObjects=_H3cSpbTrapsObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,128,1,3,1))
_H3cSpbConflictSysID_Type=MacAddress
_H3cSpbConflictSysID_Object=MibScalar
h3cSpbConflictSysID=_H3cSpbConflictSysID_Object((1,3,6,1,4,1,2011,10,2,128,1,3,1,1),_H3cSpbConflictSysID_Type())
h3cSpbConflictSysID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSpbConflictSysID.setStatus(_A)
_H3cSpbConflictSPSourceID_Type=IEEE8021SpbmSPsourceId
_H3cSpbConflictSPSourceID_Object=MibScalar
h3cSpbConflictSPSourceID=_H3cSpbConflictSPSourceID_Object((1,3,6,1,4,1,2011,10,2,128,1,3,1,2),_H3cSpbConflictSPSourceID_Type())
h3cSpbConflictSPSourceID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSpbConflictSPSourceID.setStatus(_A)
_H3cSpbConflictBMac_Type=MacAddress
_H3cSpbConflictBMac_Object=MibScalar
h3cSpbConflictBMac=_H3cSpbConflictBMac_Object((1,3,6,1,4,1,2011,10,2,128,1,3,1,3),_H3cSpbConflictBMac_Type())
h3cSpbConflictBMac.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSpbConflictBMac.setStatus(_A)
h3cSpbSPSourceConflictTrap=NotificationType((1,3,6,1,4,1,2011,10,2,128,1,3,0,1))
h3cSpbSPSourceConflictTrap.setObjects(*((_B,_H),(_B,_O)))
if mibBuilder.loadTexts:h3cSpbSPSourceConflictTrap.setStatus(_A)
h3cSpbBMacConflictTrap=NotificationType((1,3,6,1,4,1,2011,10,2,128,1,3,0,2))
h3cSpbBMacConflictTrap.setObjects(*((_B,_H),(_B,_P)))
if mibBuilder.loadTexts:h3cSpbBMacConflictTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSpb':h3cSpb,'h3cSpbObjects':h3cSpbObjects,'h3cSpbSysObjects':h3cSpbSysObjects,'h3cSpbSysStatus':h3cSpbSysStatus,'h3cSpbMulticastBVlanStatus':h3cSpbMulticastBVlanStatus,'h3cSpbConfig':h3cSpbConfig,'h3cSpbIfTable':h3cSpbIfTable,'h3cSpbIfEntry':h3cSpbIfEntry,'h3cSpbIfStatus':h3cSpbIfStatus,'h3cSpbSrvTable':h3cSpbSrvTable,'h3cSpbSrvEntry':h3cSpbSrvEntry,_L:h3cSpbSrvTableEntryTopIx,_M:h3cSpbSrvTableEntryIsid,'h3cSpbSrvTableEntryBaseVid':h3cSpbSrvTableEntryBaseVid,'h3cSpbSrvTableEntryMode':h3cSpbSrvTableEntryMode,'h3cSpbTrap':h3cSpbTrap,'h3cSpbTraps':h3cSpbTraps,'h3cSpbSPSourceConflictTrap':h3cSpbSPSourceConflictTrap,'h3cSpbBMacConflictTrap':h3cSpbBMacConflictTrap,'h3cSpbTrapsObjects':h3cSpbTrapsObjects,_H:h3cSpbConflictSysID,_O:h3cSpbConflictSPSourceID,_P:h3cSpbConflictBMac})