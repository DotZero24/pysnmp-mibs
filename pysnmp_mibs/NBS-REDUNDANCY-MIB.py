_V='nbsRedundCfgStatusOper'
_U='enabled'
_T='disabled'
_S='nbsRedundGroupCfgNumber'
_R='nbsRedundGroupCfgNdx'
_Q='access'
_P='active'
_O='standby'
_N='nbsRedundCfgNdx'
_M='nbsCmmcSlotIndex'
_L='nbsCmmcPortIndex'
_K='nbsCmmcChassisIndex'
_J='OctetString'
_I='read-create'
_H='not-accessible'
_G='NBS-CMMC-MIB'
_F='NBS-REDUNDANCY-MIB'
_E='read-write'
_D='read-only'
_C='notSupported'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbsCmmcChassisIndex,nbsCmmcPortIndex,nbsCmmcSlotIndex=mibBuilder.importSymbols(_G,_K,_L,_M)
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
nbsRedundancyMib=ModuleIdentity((1,3,6,1,4,1,629,221))
_NbsRedundCfgGrp_ObjectIdentity=ObjectIdentity
nbsRedundCfgGrp=_NbsRedundCfgGrp_ObjectIdentity((1,3,6,1,4,1,629,221,1))
if mibBuilder.loadTexts:nbsRedundCfgGrp.setStatus(_A)
_NbsRedundCfgTableSize_Type=Integer32
_NbsRedundCfgTableSize_Object=MibScalar
nbsRedundCfgTableSize=_NbsRedundCfgTableSize_Object((1,3,6,1,4,1,629,221,1,1),_NbsRedundCfgTableSize_Type())
nbsRedundCfgTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundCfgTableSize.setStatus(_A)
_NbsRedundCfgTable_Object=MibTable
nbsRedundCfgTable=_NbsRedundCfgTable_Object((1,3,6,1,4,1,629,221,1,2))
if mibBuilder.loadTexts:nbsRedundCfgTable.setStatus(_A)
_NbsRedundCfgEntry_Object=MibTableRow
nbsRedundCfgEntry=_NbsRedundCfgEntry_Object((1,3,6,1,4,1,629,221,1,2,1))
nbsRedundCfgEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:nbsRedundCfgEntry.setStatus(_A)
_NbsRedundCfgNdx_Type=InterfaceIndex
_NbsRedundCfgNdx_Object=MibTableColumn
nbsRedundCfgNdx=_NbsRedundCfgNdx_Object((1,3,6,1,4,1,629,221,1,2,1,1),_NbsRedundCfgNdx_Type())
nbsRedundCfgNdx.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsRedundCfgNdx.setStatus(_A)
_NbsRedundCfgPartnerNdxAdmin_Type=InterfaceIndex
_NbsRedundCfgPartnerNdxAdmin_Object=MibTableColumn
nbsRedundCfgPartnerNdxAdmin=_NbsRedundCfgPartnerNdxAdmin_Object((1,3,6,1,4,1,629,221,1,2,1,2),_NbsRedundCfgPartnerNdxAdmin_Type())
nbsRedundCfgPartnerNdxAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRedundCfgPartnerNdxAdmin.setStatus(_A)
_NbsRedundCfgPartnerNdxOper_Type=InterfaceIndex
_NbsRedundCfgPartnerNdxOper_Object=MibTableColumn
nbsRedundCfgPartnerNdxOper=_NbsRedundCfgPartnerNdxOper_Object((1,3,6,1,4,1,629,221,1,2,1,3),_NbsRedundCfgPartnerNdxOper_Type())
nbsRedundCfgPartnerNdxOper.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundCfgPartnerNdxOper.setStatus(_A)
class _NbsRedundCfgStatusAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_O,2),(_P,3)))
_NbsRedundCfgStatusAdmin_Type.__name__=_B
_NbsRedundCfgStatusAdmin_Object=MibTableColumn
nbsRedundCfgStatusAdmin=_NbsRedundCfgStatusAdmin_Object((1,3,6,1,4,1,629,221,1,2,1,10),_NbsRedundCfgStatusAdmin_Type())
nbsRedundCfgStatusAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRedundCfgStatusAdmin.setStatus(_A)
class _NbsRedundCfgStatusOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_O,2),(_P,3)))
_NbsRedundCfgStatusOper_Type.__name__=_B
_NbsRedundCfgStatusOper_Object=MibTableColumn
nbsRedundCfgStatusOper=_NbsRedundCfgStatusOper_Object((1,3,6,1,4,1,629,221,1,2,1,11),_NbsRedundCfgStatusOper_Type())
nbsRedundCfgStatusOper.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundCfgStatusOper.setStatus(_A)
class _NbsRedundCfgPreferredAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),('preferNot',2),('preferActive',3)))
_NbsRedundCfgPreferredAdmin_Type.__name__=_B
_NbsRedundCfgPreferredAdmin_Object=MibTableColumn
nbsRedundCfgPreferredAdmin=_NbsRedundCfgPreferredAdmin_Object((1,3,6,1,4,1,629,221,1,2,1,20),_NbsRedundCfgPreferredAdmin_Type())
nbsRedundCfgPreferredAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRedundCfgPreferredAdmin.setStatus(_A)
class _NbsRedundCfgStandbyTxAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),('standbyCold',2),('standbyHot',3)))
_NbsRedundCfgStandbyTxAdmin_Type.__name__=_B
_NbsRedundCfgStandbyTxAdmin_Object=MibTableColumn
nbsRedundCfgStandbyTxAdmin=_NbsRedundCfgStandbyTxAdmin_Object((1,3,6,1,4,1,629,221,1,2,1,30),_NbsRedundCfgStandbyTxAdmin_Type())
nbsRedundCfgStandbyTxAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRedundCfgStandbyTxAdmin.setStatus(_A)
class _NbsRedundCfgStandbyTxToggle_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),('txOff',2),('txToggle',3)))
_NbsRedundCfgStandbyTxToggle_Type.__name__=_B
_NbsRedundCfgStandbyTxToggle_Object=MibTableColumn
nbsRedundCfgStandbyTxToggle=_NbsRedundCfgStandbyTxToggle_Object((1,3,6,1,4,1,629,221,1,2,1,40),_NbsRedundCfgStandbyTxToggle_Type())
nbsRedundCfgStandbyTxToggle.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRedundCfgStandbyTxToggle.setStatus(_A)
class _NbsRedundCfgIfTypeAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_Q,2),('trunk',3)))
_NbsRedundCfgIfTypeAdmin_Type.__name__=_B
_NbsRedundCfgIfTypeAdmin_Object=MibTableColumn
nbsRedundCfgIfTypeAdmin=_NbsRedundCfgIfTypeAdmin_Object((1,3,6,1,4,1,629,221,1,2,1,50),_NbsRedundCfgIfTypeAdmin_Type())
nbsRedundCfgIfTypeAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRedundCfgIfTypeAdmin.setStatus(_A)
class _NbsRedundCfgIfTypeOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_Q,2),('trunk',3)))
_NbsRedundCfgIfTypeOper_Type.__name__=_B
_NbsRedundCfgIfTypeOper_Object=MibTableColumn
nbsRedundCfgIfTypeOper=_NbsRedundCfgIfTypeOper_Object((1,3,6,1,4,1,629,221,1,2,1,51),_NbsRedundCfgIfTypeOper_Type())
nbsRedundCfgIfTypeOper.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundCfgIfTypeOper.setStatus(_A)
_NbsRedundCfgGroupNumberAdmin_Type=Integer32
_NbsRedundCfgGroupNumberAdmin_Object=MibTableColumn
nbsRedundCfgGroupNumberAdmin=_NbsRedundCfgGroupNumberAdmin_Object((1,3,6,1,4,1,629,221,1,2,1,60),_NbsRedundCfgGroupNumberAdmin_Type())
nbsRedundCfgGroupNumberAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsRedundCfgGroupNumberAdmin.setStatus(_A)
_NbsRedundCfgGroupNumberOper_Type=Integer32
_NbsRedundCfgGroupNumberOper_Object=MibTableColumn
nbsRedundCfgGroupNumberOper=_NbsRedundCfgGroupNumberOper_Object((1,3,6,1,4,1,629,221,1,2,1,61),_NbsRedundCfgGroupNumberOper_Type())
nbsRedundCfgGroupNumberOper.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundCfgGroupNumberOper.setStatus(_A)
_NbsRedundGroupCfgTableSize_Type=Integer32
_NbsRedundGroupCfgTableSize_Object=MibScalar
nbsRedundGroupCfgTableSize=_NbsRedundGroupCfgTableSize_Object((1,3,6,1,4,1,629,221,1,3),_NbsRedundGroupCfgTableSize_Type())
nbsRedundGroupCfgTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundGroupCfgTableSize.setStatus(_A)
_NbsRedundGroupCfgTable_Object=MibTable
nbsRedundGroupCfgTable=_NbsRedundGroupCfgTable_Object((1,3,6,1,4,1,629,221,1,4))
if mibBuilder.loadTexts:nbsRedundGroupCfgTable.setStatus(_A)
_NbsRedundGroupCfgEntry_Object=MibTableRow
nbsRedundGroupCfgEntry=_NbsRedundGroupCfgEntry_Object((1,3,6,1,4,1,629,221,1,4,1))
nbsRedundGroupCfgEntry.setIndexNames((0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:nbsRedundGroupCfgEntry.setStatus(_A)
_NbsRedundGroupCfgNdx_Type=InterfaceIndex
_NbsRedundGroupCfgNdx_Object=MibTableColumn
nbsRedundGroupCfgNdx=_NbsRedundGroupCfgNdx_Object((1,3,6,1,4,1,629,221,1,4,1,1),_NbsRedundGroupCfgNdx_Type())
nbsRedundGroupCfgNdx.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsRedundGroupCfgNdx.setStatus(_A)
_NbsRedundGroupCfgNumber_Type=Integer32
_NbsRedundGroupCfgNumber_Object=MibTableColumn
nbsRedundGroupCfgNumber=_NbsRedundGroupCfgNumber_Object((1,3,6,1,4,1,629,221,1,4,1,2),_NbsRedundGroupCfgNumber_Type())
nbsRedundGroupCfgNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsRedundGroupCfgNumber.setStatus(_A)
class _NbsRedundGroupCfgOper_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsRedundGroupCfgOper_Type.__name__=_J
_NbsRedundGroupCfgOper_Object=MibTableColumn
nbsRedundGroupCfgOper=_NbsRedundGroupCfgOper_Object((1,3,6,1,4,1,629,221,1,4,1,13),_NbsRedundGroupCfgOper_Type())
nbsRedundGroupCfgOper.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundGroupCfgOper.setStatus(_A)
class _NbsRedundGroupCfgModeAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),('modeA',2),('modeB',3)))
_NbsRedundGroupCfgModeAdmin_Type.__name__=_B
_NbsRedundGroupCfgModeAdmin_Object=MibTableColumn
nbsRedundGroupCfgModeAdmin=_NbsRedundGroupCfgModeAdmin_Object((1,3,6,1,4,1,629,221,1,4,1,15),_NbsRedundGroupCfgModeAdmin_Type())
nbsRedundGroupCfgModeAdmin.setMaxAccess(_I)
if mibBuilder.loadTexts:nbsRedundGroupCfgModeAdmin.setStatus(_A)
class _NbsRedundGroupCfgModeOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),('modeA',2),('modeB',3)))
_NbsRedundGroupCfgModeOper_Type.__name__=_B
_NbsRedundGroupCfgModeOper_Object=MibTableColumn
nbsRedundGroupCfgModeOper=_NbsRedundGroupCfgModeOper_Object((1,3,6,1,4,1,629,221,1,4,1,16),_NbsRedundGroupCfgModeOper_Type())
nbsRedundGroupCfgModeOper.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundGroupCfgModeOper.setStatus(_A)
class _NbsRedundGroupCfgYcableAdmin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_T,2),(_U,3)))
_NbsRedundGroupCfgYcableAdmin_Type.__name__=_B
_NbsRedundGroupCfgYcableAdmin_Object=MibTableColumn
nbsRedundGroupCfgYcableAdmin=_NbsRedundGroupCfgYcableAdmin_Object((1,3,6,1,4,1,629,221,1,4,1,20),_NbsRedundGroupCfgYcableAdmin_Type())
nbsRedundGroupCfgYcableAdmin.setMaxAccess(_I)
if mibBuilder.loadTexts:nbsRedundGroupCfgYcableAdmin.setStatus(_A)
class _NbsRedundGroupCfgYcableOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_T,2),(_U,3)))
_NbsRedundGroupCfgYcableOper_Type.__name__=_B
_NbsRedundGroupCfgYcableOper_Object=MibTableColumn
nbsRedundGroupCfgYcableOper=_NbsRedundGroupCfgYcableOper_Object((1,3,6,1,4,1,629,221,1,4,1,21),_NbsRedundGroupCfgYcableOper_Type())
nbsRedundGroupCfgYcableOper.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsRedundGroupCfgYcableOper.setStatus(_A)
_NbsRedundGroupCfgRowStatus_Type=RowStatus
_NbsRedundGroupCfgRowStatus_Object=MibTableColumn
nbsRedundGroupCfgRowStatus=_NbsRedundGroupCfgRowStatus_Object((1,3,6,1,4,1,629,221,1,4,1,50),_NbsRedundGroupCfgRowStatus_Type())
nbsRedundGroupCfgRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:nbsRedundGroupCfgRowStatus.setStatus(_A)
_NbsRedundEventGrp_ObjectIdentity=ObjectIdentity
nbsRedundEventGrp=_NbsRedundEventGrp_ObjectIdentity((1,3,6,1,4,1,629,221,100))
if mibBuilder.loadTexts:nbsRedundEventGrp.setStatus(_A)
_NbsYcableTraps_ObjectIdentity=ObjectIdentity
nbsYcableTraps=_NbsYcableTraps_ObjectIdentity((1,3,6,1,4,1,629,221,100,0))
if mibBuilder.loadTexts:nbsYcableTraps.setStatus(_A)
nbsYcableTrapsStatusChanged=NotificationType((1,3,6,1,4,1,629,221,100,0,10))
nbsYcableTrapsStatusChanged.setObjects(*((_G,_K),(_G,_M),(_G,_L),(_F,_V)))
if mibBuilder.loadTexts:nbsYcableTrapsStatusChanged.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'nbsRedundancyMib':nbsRedundancyMib,'nbsRedundCfgGrp':nbsRedundCfgGrp,'nbsRedundCfgTableSize':nbsRedundCfgTableSize,'nbsRedundCfgTable':nbsRedundCfgTable,'nbsRedundCfgEntry':nbsRedundCfgEntry,_N:nbsRedundCfgNdx,'nbsRedundCfgPartnerNdxAdmin':nbsRedundCfgPartnerNdxAdmin,'nbsRedundCfgPartnerNdxOper':nbsRedundCfgPartnerNdxOper,'nbsRedundCfgStatusAdmin':nbsRedundCfgStatusAdmin,_V:nbsRedundCfgStatusOper,'nbsRedundCfgPreferredAdmin':nbsRedundCfgPreferredAdmin,'nbsRedundCfgStandbyTxAdmin':nbsRedundCfgStandbyTxAdmin,'nbsRedundCfgStandbyTxToggle':nbsRedundCfgStandbyTxToggle,'nbsRedundCfgIfTypeAdmin':nbsRedundCfgIfTypeAdmin,'nbsRedundCfgIfTypeOper':nbsRedundCfgIfTypeOper,'nbsRedundCfgGroupNumberAdmin':nbsRedundCfgGroupNumberAdmin,'nbsRedundCfgGroupNumberOper':nbsRedundCfgGroupNumberOper,'nbsRedundGroupCfgTableSize':nbsRedundGroupCfgTableSize,'nbsRedundGroupCfgTable':nbsRedundGroupCfgTable,'nbsRedundGroupCfgEntry':nbsRedundGroupCfgEntry,_R:nbsRedundGroupCfgNdx,_S:nbsRedundGroupCfgNumber,'nbsRedundGroupCfgOper':nbsRedundGroupCfgOper,'nbsRedundGroupCfgModeAdmin':nbsRedundGroupCfgModeAdmin,'nbsRedundGroupCfgModeOper':nbsRedundGroupCfgModeOper,'nbsRedundGroupCfgYcableAdmin':nbsRedundGroupCfgYcableAdmin,'nbsRedundGroupCfgYcableOper':nbsRedundGroupCfgYcableOper,'nbsRedundGroupCfgRowStatus':nbsRedundGroupCfgRowStatus,'nbsRedundEventGrp':nbsRedundEventGrp,'nbsYcableTraps':nbsYcableTraps,'nbsYcableTrapsStatusChanged':nbsYcableTrapsStatusChanged})