_P='hpnicfSpbConflictBMac'
_O='hpnicfSpbConflictSPSourceID'
_N='not-accessible'
_M='hpnicfSpbSrvTableEntryIsid'
_L='hpnicfSpbSrvTableEntryTopIx'
_K='Unsigned32'
_J='ifIndex'
_I='IF-MIB'
_H='hpnicfSpbConflictSysID'
_G='accessible-for-notify'
_F='disabled'
_E='enabled'
_D='read-write'
_C='Integer32'
_B='HPN-ICF-SPB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
IEEE8021SpbmSPsourceId,=mibBuilder.importSymbols('IEEE8021-SPB-MIB','IEEE8021SpbmSPsourceId')
ifIndex,=mibBuilder.importSymbols(_I,_J)
VlanIdOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIdOrNone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpnicfSpb=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,128))
if mibBuilder.loadTexts:hpnicfSpb.setRevisions(('2012-11-22 00:00',))
_HpnicfSpbObjects_ObjectIdentity=ObjectIdentity
hpnicfSpbObjects=_HpnicfSpbObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,128,1))
_HpnicfSpbSysObjects_ObjectIdentity=ObjectIdentity
hpnicfSpbSysObjects=_HpnicfSpbSysObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,128,1,1))
class _HpnicfSpbSysStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpnicfSpbSysStatus_Type.__name__=_C
_HpnicfSpbSysStatus_Object=MibScalar
hpnicfSpbSysStatus=_HpnicfSpbSysStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,1,1),_HpnicfSpbSysStatus_Type())
hpnicfSpbSysStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSpbSysStatus.setStatus(_A)
class _HpnicfSpbMulticastBVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpnicfSpbMulticastBVlanStatus_Type.__name__=_C
_HpnicfSpbMulticastBVlanStatus_Object=MibScalar
hpnicfSpbMulticastBVlanStatus=_HpnicfSpbMulticastBVlanStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,1,2),_HpnicfSpbMulticastBVlanStatus_Type())
hpnicfSpbMulticastBVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSpbMulticastBVlanStatus.setStatus(_A)
_HpnicfSpbConfig_ObjectIdentity=ObjectIdentity
hpnicfSpbConfig=_HpnicfSpbConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2))
_HpnicfSpbIfTable_Object=MibTable
hpnicfSpbIfTable=_HpnicfSpbIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,1))
if mibBuilder.loadTexts:hpnicfSpbIfTable.setStatus(_A)
_HpnicfSpbIfEntry_Object=MibTableRow
hpnicfSpbIfEntry=_HpnicfSpbIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,1,1))
hpnicfSpbIfEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfSpbIfEntry.setStatus(_A)
class _HpnicfSpbIfStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpnicfSpbIfStatus_Type.__name__=_C
_HpnicfSpbIfStatus_Object=MibTableColumn
hpnicfSpbIfStatus=_HpnicfSpbIfStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,1,1,1),_HpnicfSpbIfStatus_Type())
hpnicfSpbIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSpbIfStatus.setStatus(_A)
_HpnicfSpbSrvTable_Object=MibTable
hpnicfSpbSrvTable=_HpnicfSpbSrvTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,2))
if mibBuilder.loadTexts:hpnicfSpbSrvTable.setStatus(_A)
_HpnicfSpbSrvEntry_Object=MibTableRow
hpnicfSpbSrvEntry=_HpnicfSpbSrvEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,2,1))
hpnicfSpbSrvEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:hpnicfSpbSrvEntry.setStatus(_A)
_HpnicfSpbSrvTableEntryTopIx_Type=Unsigned32
_HpnicfSpbSrvTableEntryTopIx_Object=MibTableColumn
hpnicfSpbSrvTableEntryTopIx=_HpnicfSpbSrvTableEntryTopIx_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,2,1,1),_HpnicfSpbSrvTableEntryTopIx_Type())
hpnicfSpbSrvTableEntryTopIx.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfSpbSrvTableEntryTopIx.setStatus(_A)
class _HpnicfSpbSrvTableEntryIsid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(255,16777215))
_HpnicfSpbSrvTableEntryIsid_Type.__name__=_K
_HpnicfSpbSrvTableEntryIsid_Object=MibTableColumn
hpnicfSpbSrvTableEntryIsid=_HpnicfSpbSrvTableEntryIsid_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,2,1,2),_HpnicfSpbSrvTableEntryIsid_Type())
hpnicfSpbSrvTableEntryIsid.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfSpbSrvTableEntryIsid.setStatus(_A)
_HpnicfSpbSrvTableEntryBaseVid_Type=VlanIdOrNone
_HpnicfSpbSrvTableEntryBaseVid_Object=MibTableColumn
hpnicfSpbSrvTableEntryBaseVid=_HpnicfSpbSrvTableEntryBaseVid_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,2,1,3),_HpnicfSpbSrvTableEntryBaseVid_Type())
hpnicfSpbSrvTableEntryBaseVid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSpbSrvTableEntryBaseVid.setStatus(_A)
class _HpnicfSpbSrvTableEntryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('headEnd',1),('tandem',2)))
_HpnicfSpbSrvTableEntryMode_Type.__name__=_C
_HpnicfSpbSrvTableEntryMode_Object=MibTableColumn
hpnicfSpbSrvTableEntryMode=_HpnicfSpbSrvTableEntryMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,2,2,1,4),_HpnicfSpbSrvTableEntryMode_Type())
hpnicfSpbSrvTableEntryMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSpbSrvTableEntryMode.setStatus(_A)
_HpnicfSpbTrap_ObjectIdentity=ObjectIdentity
hpnicfSpbTrap=_HpnicfSpbTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3))
_HpnicfSpbTraps_ObjectIdentity=ObjectIdentity
hpnicfSpbTraps=_HpnicfSpbTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3,0))
_HpnicfSpbTrapsObjects_ObjectIdentity=ObjectIdentity
hpnicfSpbTrapsObjects=_HpnicfSpbTrapsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3,1))
_HpnicfSpbConflictSysID_Type=MacAddress
_HpnicfSpbConflictSysID_Object=MibScalar
hpnicfSpbConflictSysID=_HpnicfSpbConflictSysID_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3,1,1),_HpnicfSpbConflictSysID_Type())
hpnicfSpbConflictSysID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSpbConflictSysID.setStatus(_A)
_HpnicfSpbConflictSPSourceID_Type=IEEE8021SpbmSPsourceId
_HpnicfSpbConflictSPSourceID_Object=MibScalar
hpnicfSpbConflictSPSourceID=_HpnicfSpbConflictSPSourceID_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3,1,2),_HpnicfSpbConflictSPSourceID_Type())
hpnicfSpbConflictSPSourceID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSpbConflictSPSourceID.setStatus(_A)
_HpnicfSpbConflictBMac_Type=MacAddress
_HpnicfSpbConflictBMac_Object=MibScalar
hpnicfSpbConflictBMac=_HpnicfSpbConflictBMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3,1,3),_HpnicfSpbConflictBMac_Type())
hpnicfSpbConflictBMac.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSpbConflictBMac.setStatus(_A)
hpnicfSpbSPSourceConflictTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3,0,1))
hpnicfSpbSPSourceConflictTrap.setObjects(*((_B,_H),(_B,_O)))
if mibBuilder.loadTexts:hpnicfSpbSPSourceConflictTrap.setStatus(_A)
hpnicfSpbBMacConflictTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,128,1,3,0,2))
hpnicfSpbBMacConflictTrap.setObjects(*((_B,_H),(_B,_P)))
if mibBuilder.loadTexts:hpnicfSpbBMacConflictTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfSpb':hpnicfSpb,'hpnicfSpbObjects':hpnicfSpbObjects,'hpnicfSpbSysObjects':hpnicfSpbSysObjects,'hpnicfSpbSysStatus':hpnicfSpbSysStatus,'hpnicfSpbMulticastBVlanStatus':hpnicfSpbMulticastBVlanStatus,'hpnicfSpbConfig':hpnicfSpbConfig,'hpnicfSpbIfTable':hpnicfSpbIfTable,'hpnicfSpbIfEntry':hpnicfSpbIfEntry,'hpnicfSpbIfStatus':hpnicfSpbIfStatus,'hpnicfSpbSrvTable':hpnicfSpbSrvTable,'hpnicfSpbSrvEntry':hpnicfSpbSrvEntry,_L:hpnicfSpbSrvTableEntryTopIx,_M:hpnicfSpbSrvTableEntryIsid,'hpnicfSpbSrvTableEntryBaseVid':hpnicfSpbSrvTableEntryBaseVid,'hpnicfSpbSrvTableEntryMode':hpnicfSpbSrvTableEntryMode,'hpnicfSpbTrap':hpnicfSpbTrap,'hpnicfSpbTraps':hpnicfSpbTraps,'hpnicfSpbSPSourceConflictTrap':hpnicfSpbSPSourceConflictTrap,'hpnicfSpbBMacConflictTrap':hpnicfSpbBMacConflictTrap,'hpnicfSpbTrapsObjects':hpnicfSpbTrapsObjects,_H:hpnicfSpbConflictSysID,_O:hpnicfSpbConflictSPSourceID,_P:hpnicfSpbConflictBMac})