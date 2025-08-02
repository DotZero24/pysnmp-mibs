_A4='stgNewCfgPortIndex'
_A3='stgNewCfgStgIndex'
_A2='stgCurCfgPortIndex'
_A1='stgCurCfgStgIndex'
_A0='stgNewCfgIndex'
_z='stgCurCfgIndex'
_y='pmNewCfgVmirrMirrVlanIndex'
_x='pmNewCfgVmirrMoniPortIndex'
_w='pmCurCfgVmirrMirrVlanIndex'
_v='pmCurCfgVmirrMoniPortIndex'
_u='pmNewCfgPmirrMirrPortIndex'
_t='pmNewCfgPmirrMoniPortIndex'
_s='pmCurCfgPmirrMirrPortIndex'
_r='pmCurCfgPmirrMoniPortIndex'
_q='portInfoIndx'
_p='portStatsIndx'
_o='portCpuStatsUtilIndx'
_n='trunkGroupNewCfgIndex'
_m='disable'
_l='enable'
_k='trunkGroupCurCfgIndex'
_j='transmitted'
_i='received'
_h='vlanNewCfgVlanId'
_g='vlanCurCfgVlanId'
_f='agPortNewCfgIndx'
_e='full-or-half-duplex'
_d='mbs10or100'
_c='untagged'
_b='tagged'
_a='agPortCurCfgIndx'
_Z='half-duplex'
_Y='full-duplex'
_X='mbs100'
_W='mbs10'
_V='delete'
_U='gigabit-ethernet'
_T='fast-ethernet'
_S='out'
_R='in'
_Q='other'
_P='receive'
_O='transmit'
_N='DisplayString'
_M='OctetString'
_L='obsolete'
_K='none'
_J='both'
_I='off'
_H='on'
_G='enabled'
_F='disabled'
_E='ALTEON-TS-PHYSICAL-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch,=mibBuilder.importSymbols('ALTEON-ROOT-MIB','switch')
agent,information,operCmds,stats=mibBuilder.importSymbols('ALTEON-TIGON-SWITCH-MIB','agent','information','operCmds','stats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
_AgPortConfig_ObjectIdentity=ObjectIdentity
agPortConfig=_AgPortConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,1,2,3))
_AgPortTableMaxEnt_Type=Integer32
_AgPortTableMaxEnt_Object=MibScalar
agPortTableMaxEnt=_AgPortTableMaxEnt_Object((1,3,6,1,4,1,1872,2,1,2,3,1),_AgPortTableMaxEnt_Type())
agPortTableMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortTableMaxEnt.setStatus(_A)
_AgPortCurCfgTable_Object=MibTable
agPortCurCfgTable=_AgPortCurCfgTable_Object((1,3,6,1,4,1,1872,2,1,2,3,2))
if mibBuilder.loadTexts:agPortCurCfgTable.setStatus(_A)
_AgPortCurCfgTableEntry_Object=MibTableRow
agPortCurCfgTableEntry=_AgPortCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1))
agPortCurCfgTableEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:agPortCurCfgTableEntry.setStatus(_A)
class _AgPortCurCfgIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgPortCurCfgIndx_Type.__name__=_C
_AgPortCurCfgIndx_Object=MibTableColumn
agPortCurCfgIndx=_AgPortCurCfgIndx_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,1),_AgPortCurCfgIndx_Type())
agPortCurCfgIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgIndx.setStatus(_A)
class _AgPortCurCfgPrefLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_T,2),(_U,3)))
_AgPortCurCfgPrefLink_Type.__name__=_C
_AgPortCurCfgPrefLink_Object=MibTableColumn
agPortCurCfgPrefLink=_AgPortCurCfgPrefLink_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,2),_AgPortCurCfgPrefLink_Type())
agPortCurCfgPrefLink.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgPrefLink.setStatus(_A)
class _AgPortCurCfgBackLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_T,2),(_U,3),(_K,4)))
_AgPortCurCfgBackLink_Type.__name__=_C
_AgPortCurCfgBackLink_Object=MibTableColumn
agPortCurCfgBackLink=_AgPortCurCfgBackLink_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,3),_AgPortCurCfgBackLink_Type())
agPortCurCfgBackLink.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgBackLink.setStatus(_A)
class _AgPortCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_AgPortCurCfgState_Type.__name__=_C
_AgPortCurCfgState_Object=MibTableColumn
agPortCurCfgState=_AgPortCurCfgState_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,4),_AgPortCurCfgState_Type())
agPortCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgState.setStatus(_A)
class _AgPortCurCfgVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_b,2),(_c,3)))
_AgPortCurCfgVlanTag_Type.__name__=_C
_AgPortCurCfgVlanTag_Object=MibTableColumn
agPortCurCfgVlanTag=_AgPortCurCfgVlanTag_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,5),_AgPortCurCfgVlanTag_Type())
agPortCurCfgVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgVlanTag.setStatus(_A)
class _AgPortCurCfgStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortCurCfgStp_Type.__name__=_C
_AgPortCurCfgStp_Object=MibTableColumn
agPortCurCfgStp=_AgPortCurCfgStp_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,6),_AgPortCurCfgStp_Type())
agPortCurCfgStp.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgStp.setStatus(_A)
class _AgPortCurCfgRmon_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortCurCfgRmon_Type.__name__=_C
_AgPortCurCfgRmon_Object=MibTableColumn
agPortCurCfgRmon=_AgPortCurCfgRmon_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,7),_AgPortCurCfgRmon_Type())
agPortCurCfgRmon.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgRmon.setStatus(_A)
class _AgPortCurCfgPVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AgPortCurCfgPVID_Type.__name__=_C
_AgPortCurCfgPVID_Object=MibTableColumn
agPortCurCfgPVID=_AgPortCurCfgPVID_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,8),_AgPortCurCfgPVID_Type())
agPortCurCfgPVID.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgPVID.setStatus(_A)
class _AgPortCurCfgFastEthAutoNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortCurCfgFastEthAutoNeg_Type.__name__=_C
_AgPortCurCfgFastEthAutoNeg_Object=MibTableColumn
agPortCurCfgFastEthAutoNeg=_AgPortCurCfgFastEthAutoNeg_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,9),_AgPortCurCfgFastEthAutoNeg_Type())
agPortCurCfgFastEthAutoNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgFastEthAutoNeg.setStatus(_A)
class _AgPortCurCfgFastEthSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_W,2),(_X,3),(_d,4)))
_AgPortCurCfgFastEthSpeed_Type.__name__=_C
_AgPortCurCfgFastEthSpeed_Object=MibTableColumn
agPortCurCfgFastEthSpeed=_AgPortCurCfgFastEthSpeed_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,10),_AgPortCurCfgFastEthSpeed_Type())
agPortCurCfgFastEthSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgFastEthSpeed.setStatus(_A)
class _AgPortCurCfgFastEthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_Y,2),(_Z,3),(_e,4)))
_AgPortCurCfgFastEthMode_Type.__name__=_C
_AgPortCurCfgFastEthMode_Object=MibTableColumn
agPortCurCfgFastEthMode=_AgPortCurCfgFastEthMode_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,11),_AgPortCurCfgFastEthMode_Type())
agPortCurCfgFastEthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgFastEthMode.setStatus(_A)
class _AgPortCurCfgFastEthFctl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_O,2),(_P,3),(_J,4),(_K,5)))
_AgPortCurCfgFastEthFctl_Type.__name__=_C
_AgPortCurCfgFastEthFctl_Object=MibTableColumn
agPortCurCfgFastEthFctl=_AgPortCurCfgFastEthFctl_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,12),_AgPortCurCfgFastEthFctl_Type())
agPortCurCfgFastEthFctl.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgFastEthFctl.setStatus(_A)
class _AgPortCurCfgGigEthAutoNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortCurCfgGigEthAutoNeg_Type.__name__=_C
_AgPortCurCfgGigEthAutoNeg_Object=MibTableColumn
agPortCurCfgGigEthAutoNeg=_AgPortCurCfgGigEthAutoNeg_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,13),_AgPortCurCfgGigEthAutoNeg_Type())
agPortCurCfgGigEthAutoNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgGigEthAutoNeg.setStatus(_A)
class _AgPortCurCfgGigEthFctl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_O,2),(_P,3),(_J,4),(_K,5)))
_AgPortCurCfgGigEthFctl_Type.__name__=_C
_AgPortCurCfgGigEthFctl_Object=MibTableColumn
agPortCurCfgGigEthFctl=_AgPortCurCfgGigEthFctl_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,14),_AgPortCurCfgGigEthFctl_Type())
agPortCurCfgGigEthFctl.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgGigEthFctl.setStatus(_A)
class _AgPortCurCfgPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AgPortCurCfgPortName_Type.__name__=_N
_AgPortCurCfgPortName_Object=MibTableColumn
agPortCurCfgPortName=_AgPortCurCfgPortName_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,15),_AgPortCurCfgPortName_Type())
agPortCurCfgPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgPortName.setStatus(_A)
_AgPortCurCfgBwmContract_Type=Integer32
_AgPortCurCfgBwmContract_Object=MibTableColumn
agPortCurCfgBwmContract=_AgPortCurCfgBwmContract_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,16),_AgPortCurCfgBwmContract_Type())
agPortCurCfgBwmContract.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgBwmContract.setStatus(_A)
class _AgPortCurCfgDiscardNonIPs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_AgPortCurCfgDiscardNonIPs_Type.__name__=_C
_AgPortCurCfgDiscardNonIPs_Object=MibTableColumn
agPortCurCfgDiscardNonIPs=_AgPortCurCfgDiscardNonIPs_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,17),_AgPortCurCfgDiscardNonIPs_Type())
agPortCurCfgDiscardNonIPs.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgDiscardNonIPs.setStatus(_A)
class _AgPortCurCfgLinkTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_AgPortCurCfgLinkTrap_Type.__name__=_C
_AgPortCurCfgLinkTrap_Object=MibTableColumn
agPortCurCfgLinkTrap=_AgPortCurCfgLinkTrap_Object((1,3,6,1,4,1,1872,2,1,2,3,2,1,18),_AgPortCurCfgLinkTrap_Type())
agPortCurCfgLinkTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortCurCfgLinkTrap.setStatus(_A)
_AgPortNewCfgTable_Object=MibTable
agPortNewCfgTable=_AgPortNewCfgTable_Object((1,3,6,1,4,1,1872,2,1,2,3,3))
if mibBuilder.loadTexts:agPortNewCfgTable.setStatus(_A)
_AgPortNewCfgTableEntry_Object=MibTableRow
agPortNewCfgTableEntry=_AgPortNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1))
agPortNewCfgTableEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:agPortNewCfgTableEntry.setStatus(_A)
class _AgPortNewCfgIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgPortNewCfgIndx_Type.__name__=_C
_AgPortNewCfgIndx_Object=MibTableColumn
agPortNewCfgIndx=_AgPortNewCfgIndx_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,1),_AgPortNewCfgIndx_Type())
agPortNewCfgIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:agPortNewCfgIndx.setStatus(_A)
class _AgPortNewCfgPrefLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_T,2),(_U,3)))
_AgPortNewCfgPrefLink_Type.__name__=_C
_AgPortNewCfgPrefLink_Object=MibTableColumn
agPortNewCfgPrefLink=_AgPortNewCfgPrefLink_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,2),_AgPortNewCfgPrefLink_Type())
agPortNewCfgPrefLink.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgPrefLink.setStatus(_A)
class _AgPortNewCfgBackLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_T,2),(_U,3),(_K,4)))
_AgPortNewCfgBackLink_Type.__name__=_C
_AgPortNewCfgBackLink_Object=MibTableColumn
agPortNewCfgBackLink=_AgPortNewCfgBackLink_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,3),_AgPortNewCfgBackLink_Type())
agPortNewCfgBackLink.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgBackLink.setStatus(_A)
class _AgPortNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_AgPortNewCfgState_Type.__name__=_C
_AgPortNewCfgState_Object=MibTableColumn
agPortNewCfgState=_AgPortNewCfgState_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,4),_AgPortNewCfgState_Type())
agPortNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgState.setStatus(_A)
class _AgPortNewCfgVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_b,2),(_c,3)))
_AgPortNewCfgVlanTag_Type.__name__=_C
_AgPortNewCfgVlanTag_Object=MibTableColumn
agPortNewCfgVlanTag=_AgPortNewCfgVlanTag_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,5),_AgPortNewCfgVlanTag_Type())
agPortNewCfgVlanTag.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgVlanTag.setStatus(_A)
class _AgPortNewCfgStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortNewCfgStp_Type.__name__=_C
_AgPortNewCfgStp_Object=MibTableColumn
agPortNewCfgStp=_AgPortNewCfgStp_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,6),_AgPortNewCfgStp_Type())
agPortNewCfgStp.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgStp.setStatus(_A)
class _AgPortNewCfgRmon_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortNewCfgRmon_Type.__name__=_C
_AgPortNewCfgRmon_Object=MibTableColumn
agPortNewCfgRmon=_AgPortNewCfgRmon_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,7),_AgPortNewCfgRmon_Type())
agPortNewCfgRmon.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgRmon.setStatus(_A)
class _AgPortNewCfgPVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AgPortNewCfgPVID_Type.__name__=_C
_AgPortNewCfgPVID_Object=MibTableColumn
agPortNewCfgPVID=_AgPortNewCfgPVID_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,8),_AgPortNewCfgPVID_Type())
agPortNewCfgPVID.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgPVID.setStatus(_A)
class _AgPortNewCfgFastEthAutoNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortNewCfgFastEthAutoNeg_Type.__name__=_C
_AgPortNewCfgFastEthAutoNeg_Object=MibTableColumn
agPortNewCfgFastEthAutoNeg=_AgPortNewCfgFastEthAutoNeg_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,9),_AgPortNewCfgFastEthAutoNeg_Type())
agPortNewCfgFastEthAutoNeg.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgFastEthAutoNeg.setStatus(_A)
class _AgPortNewCfgFastEthSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_W,2),(_X,3),(_d,4)))
_AgPortNewCfgFastEthSpeed_Type.__name__=_C
_AgPortNewCfgFastEthSpeed_Object=MibTableColumn
agPortNewCfgFastEthSpeed=_AgPortNewCfgFastEthSpeed_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,10),_AgPortNewCfgFastEthSpeed_Type())
agPortNewCfgFastEthSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgFastEthSpeed.setStatus(_A)
class _AgPortNewCfgFastEthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_Y,2),(_Z,3),(_e,4)))
_AgPortNewCfgFastEthMode_Type.__name__=_C
_AgPortNewCfgFastEthMode_Object=MibTableColumn
agPortNewCfgFastEthMode=_AgPortNewCfgFastEthMode_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,11),_AgPortNewCfgFastEthMode_Type())
agPortNewCfgFastEthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgFastEthMode.setStatus(_A)
class _AgPortNewCfgFastEthFctl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_O,2),(_P,3),(_J,4),(_K,5)))
_AgPortNewCfgFastEthFctl_Type.__name__=_C
_AgPortNewCfgFastEthFctl_Object=MibTableColumn
agPortNewCfgFastEthFctl=_AgPortNewCfgFastEthFctl_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,12),_AgPortNewCfgFastEthFctl_Type())
agPortNewCfgFastEthFctl.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgFastEthFctl.setStatus(_A)
class _AgPortNewCfgGigEthAutoNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_AgPortNewCfgGigEthAutoNeg_Type.__name__=_C
_AgPortNewCfgGigEthAutoNeg_Object=MibTableColumn
agPortNewCfgGigEthAutoNeg=_AgPortNewCfgGigEthAutoNeg_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,13),_AgPortNewCfgGigEthAutoNeg_Type())
agPortNewCfgGigEthAutoNeg.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgGigEthAutoNeg.setStatus(_A)
class _AgPortNewCfgGigEthFctl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_O,2),(_P,3),(_J,4),(_K,5)))
_AgPortNewCfgGigEthFctl_Type.__name__=_C
_AgPortNewCfgGigEthFctl_Object=MibTableColumn
agPortNewCfgGigEthFctl=_AgPortNewCfgGigEthFctl_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,14),_AgPortNewCfgGigEthFctl_Type())
agPortNewCfgGigEthFctl.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgGigEthFctl.setStatus(_A)
class _AgPortNewCfgPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AgPortNewCfgPortName_Type.__name__=_N
_AgPortNewCfgPortName_Object=MibTableColumn
agPortNewCfgPortName=_AgPortNewCfgPortName_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,15),_AgPortNewCfgPortName_Type())
agPortNewCfgPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgPortName.setStatus(_A)
_AgPortNewCfgBwmContract_Type=Integer32
_AgPortNewCfgBwmContract_Object=MibTableColumn
agPortNewCfgBwmContract=_AgPortNewCfgBwmContract_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,16),_AgPortNewCfgBwmContract_Type())
agPortNewCfgBwmContract.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgBwmContract.setStatus(_A)
class _AgPortNewCfgDiscardNonIPs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_AgPortNewCfgDiscardNonIPs_Type.__name__=_C
_AgPortNewCfgDiscardNonIPs_Object=MibTableColumn
agPortNewCfgDiscardNonIPs=_AgPortNewCfgDiscardNonIPs_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,17),_AgPortNewCfgDiscardNonIPs_Type())
agPortNewCfgDiscardNonIPs.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgDiscardNonIPs.setStatus(_A)
class _AgPortNewCfgLinkTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_AgPortNewCfgLinkTrap_Type.__name__=_C
_AgPortNewCfgLinkTrap_Object=MibTableColumn
agPortNewCfgLinkTrap=_AgPortNewCfgLinkTrap_Object((1,3,6,1,4,1,1872,2,1,2,3,3,1,18),_AgPortNewCfgLinkTrap_Type())
agPortNewCfgLinkTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:agPortNewCfgLinkTrap.setStatus(_A)
_Vlans_ObjectIdentity=ObjectIdentity
vlans=_Vlans_ObjectIdentity((1,3,6,1,4,1,1872,2,1,4))
_VlanMaxEnt_Type=Integer32
_VlanMaxEnt_Object=MibScalar
vlanMaxEnt=_VlanMaxEnt_Object((1,3,6,1,4,1,1872,2,1,4,1),_VlanMaxEnt_Type())
vlanMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMaxEnt.setStatus(_A)
_VlanCurCfgTable_Object=MibTable
vlanCurCfgTable=_VlanCurCfgTable_Object((1,3,6,1,4,1,1872,2,1,4,2))
if mibBuilder.loadTexts:vlanCurCfgTable.setStatus(_A)
_VlanCurCfgTableEntry_Object=MibTableRow
vlanCurCfgTableEntry=_VlanCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,4,2,1))
vlanCurCfgTableEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:vlanCurCfgTableEntry.setStatus(_A)
class _VlanCurCfgVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanCurCfgVlanId_Type.__name__=_C
_VlanCurCfgVlanId_Object=MibTableColumn
vlanCurCfgVlanId=_VlanCurCfgVlanId_Object((1,3,6,1,4,1,1872,2,1,4,2,1,1),_VlanCurCfgVlanId_Type())
vlanCurCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgVlanId.setStatus(_A)
class _VlanCurCfgVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanCurCfgVlanName_Type.__name__=_N
_VlanCurCfgVlanName_Object=MibTableColumn
vlanCurCfgVlanName=_VlanCurCfgVlanName_Object((1,3,6,1,4,1,1872,2,1,4,2,1,2),_VlanCurCfgVlanName_Type())
vlanCurCfgVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgVlanName.setStatus(_A)
class _VlanCurCfgPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VlanCurCfgPorts_Type.__name__=_M
_VlanCurCfgPorts_Object=MibTableColumn
vlanCurCfgPorts=_VlanCurCfgPorts_Object((1,3,6,1,4,1,1872,2,1,4,2,1,3),_VlanCurCfgPorts_Type())
vlanCurCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgPorts.setStatus(_A)
class _VlanCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_VlanCurCfgState_Type.__name__=_C
_VlanCurCfgState_Object=MibTableColumn
vlanCurCfgState=_VlanCurCfgState_Object((1,3,6,1,4,1,1872,2,1,4,2,1,4),_VlanCurCfgState_Type())
vlanCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgState.setStatus(_A)
class _VlanCurCfgJumbo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_VlanCurCfgJumbo_Type.__name__=_C
_VlanCurCfgJumbo_Object=MibTableColumn
vlanCurCfgJumbo=_VlanCurCfgJumbo_Object((1,3,6,1,4,1,1872,2,1,4,2,1,5),_VlanCurCfgJumbo_Type())
vlanCurCfgJumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgJumbo.setStatus(_A)
_VlanCurCfgBwmContract_Type=Integer32
_VlanCurCfgBwmContract_Object=MibTableColumn
vlanCurCfgBwmContract=_VlanCurCfgBwmContract_Object((1,3,6,1,4,1,1872,2,1,4,2,1,6),_VlanCurCfgBwmContract_Type())
vlanCurCfgBwmContract.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgBwmContract.setStatus(_A)
_VlanCurCfgStg_Type=Integer32
_VlanCurCfgStg_Object=MibTableColumn
vlanCurCfgStg=_VlanCurCfgStg_Object((1,3,6,1,4,1,1872,2,1,4,2,1,7),_VlanCurCfgStg_Type())
vlanCurCfgStg.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCurCfgStg.setStatus(_A)
_VlanNewCfgTable_Object=MibTable
vlanNewCfgTable=_VlanNewCfgTable_Object((1,3,6,1,4,1,1872,2,1,4,3))
if mibBuilder.loadTexts:vlanNewCfgTable.setStatus(_A)
_VlanNewCfgTableEntry_Object=MibTableRow
vlanNewCfgTableEntry=_VlanNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,4,3,1))
vlanNewCfgTableEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:vlanNewCfgTableEntry.setStatus(_A)
class _VlanNewCfgVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanNewCfgVlanId_Type.__name__=_C
_VlanNewCfgVlanId_Object=MibTableColumn
vlanNewCfgVlanId=_VlanNewCfgVlanId_Object((1,3,6,1,4,1,1872,2,1,4,3,1,1),_VlanNewCfgVlanId_Type())
vlanNewCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNewCfgVlanId.setStatus(_A)
class _VlanNewCfgVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanNewCfgVlanName_Type.__name__=_N
_VlanNewCfgVlanName_Object=MibTableColumn
vlanNewCfgVlanName=_VlanNewCfgVlanName_Object((1,3,6,1,4,1,1872,2,1,4,3,1,2),_VlanNewCfgVlanName_Type())
vlanNewCfgVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgVlanName.setStatus(_A)
class _VlanNewCfgPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VlanNewCfgPorts_Type.__name__=_M
_VlanNewCfgPorts_Object=MibTableColumn
vlanNewCfgPorts=_VlanNewCfgPorts_Object((1,3,6,1,4,1,1872,2,1,4,3,1,3),_VlanNewCfgPorts_Type())
vlanNewCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanNewCfgPorts.setStatus(_A)
class _VlanNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_VlanNewCfgState_Type.__name__=_C
_VlanNewCfgState_Object=MibTableColumn
vlanNewCfgState=_VlanNewCfgState_Object((1,3,6,1,4,1,1872,2,1,4,3,1,4),_VlanNewCfgState_Type())
vlanNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgState.setStatus(_A)
class _VlanNewCfgJumbo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_VlanNewCfgJumbo_Type.__name__=_C
_VlanNewCfgJumbo_Object=MibTableColumn
vlanNewCfgJumbo=_VlanNewCfgJumbo_Object((1,3,6,1,4,1,1872,2,1,4,3,1,5),_VlanNewCfgJumbo_Type())
vlanNewCfgJumbo.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgJumbo.setStatus(_A)
_VlanNewCfgAddPort_Type=Integer32
_VlanNewCfgAddPort_Object=MibTableColumn
vlanNewCfgAddPort=_VlanNewCfgAddPort_Object((1,3,6,1,4,1,1872,2,1,4,3,1,6),_VlanNewCfgAddPort_Type())
vlanNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgAddPort.setStatus(_A)
_VlanNewCfgRemovePort_Type=Integer32
_VlanNewCfgRemovePort_Object=MibTableColumn
vlanNewCfgRemovePort=_VlanNewCfgRemovePort_Object((1,3,6,1,4,1,1872,2,1,4,3,1,7),_VlanNewCfgRemovePort_Type())
vlanNewCfgRemovePort.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgRemovePort.setStatus(_A)
class _VlanNewCfgDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_V,2)))
_VlanNewCfgDelete_Type.__name__=_C
_VlanNewCfgDelete_Object=MibTableColumn
vlanNewCfgDelete=_VlanNewCfgDelete_Object((1,3,6,1,4,1,1872,2,1,4,3,1,8),_VlanNewCfgDelete_Type())
vlanNewCfgDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgDelete.setStatus(_A)
_VlanNewCfgBwmContract_Type=Integer32
_VlanNewCfgBwmContract_Object=MibTableColumn
vlanNewCfgBwmContract=_VlanNewCfgBwmContract_Object((1,3,6,1,4,1,1872,2,1,4,3,1,9),_VlanNewCfgBwmContract_Type())
vlanNewCfgBwmContract.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgBwmContract.setStatus(_A)
_VlanNewCfgStg_Type=Integer32
_VlanNewCfgStg_Object=MibTableColumn
vlanNewCfgStg=_VlanNewCfgStg_Object((1,3,6,1,4,1,1872,2,1,4,3,1,10),_VlanNewCfgStg_Type())
vlanNewCfgStg.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNewCfgStg.setStatus(_A)
_Portmirroring_ObjectIdentity=ObjectIdentity
portmirroring=_Portmirroring_ObjectIdentity((1,3,6,1,4,1,1872,2,1,6))
_PmCurCfgMonitoringPort_Type=Integer32
_PmCurCfgMonitoringPort_Object=MibScalar
pmCurCfgMonitoringPort=_PmCurCfgMonitoringPort_Object((1,3,6,1,4,1,1872,2,1,6,1),_PmCurCfgMonitoringPort_Type())
pmCurCfgMonitoringPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgMonitoringPort.setStatus(_L)
_PmNewCfgMonitoringPort_Type=Integer32
_PmNewCfgMonitoringPort_Object=MibScalar
pmNewCfgMonitoringPort=_PmNewCfgMonitoringPort_Object((1,3,6,1,4,1,1872,2,1,6,2),_PmNewCfgMonitoringPort_Type())
pmNewCfgMonitoringPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgMonitoringPort.setStatus(_L)
_PmCurCfgMirroredPort_Type=Integer32
_PmCurCfgMirroredPort_Object=MibScalar
pmCurCfgMirroredPort=_PmCurCfgMirroredPort_Object((1,3,6,1,4,1,1872,2,1,6,3),_PmCurCfgMirroredPort_Type())
pmCurCfgMirroredPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgMirroredPort.setStatus(_L)
_PmNewCfgMirroredPort_Type=Integer32
_PmNewCfgMirroredPort_Object=MibScalar
pmNewCfgMirroredPort=_PmNewCfgMirroredPort_Object((1,3,6,1,4,1,1872,2,1,6,4),_PmNewCfgMirroredPort_Type())
pmNewCfgMirroredPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgMirroredPort.setStatus(_L)
class _PmCurCfgMonitoredTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_K,2),(_i,3),(_j,4),(_J,5)))
_PmCurCfgMonitoredTraffic_Type.__name__=_C
_PmCurCfgMonitoredTraffic_Object=MibScalar
pmCurCfgMonitoredTraffic=_PmCurCfgMonitoredTraffic_Object((1,3,6,1,4,1,1872,2,1,6,5),_PmCurCfgMonitoredTraffic_Type())
pmCurCfgMonitoredTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgMonitoredTraffic.setStatus(_L)
class _PmNewCfgMonitoredTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_K,2),(_i,3),(_j,4),(_J,5)))
_PmNewCfgMonitoredTraffic_Type.__name__=_C
_PmNewCfgMonitoredTraffic_Object=MibScalar
pmNewCfgMonitoredTraffic=_PmNewCfgMonitoredTraffic_Object((1,3,6,1,4,1,1872,2,1,6,6),_PmNewCfgMonitoredTraffic_Type())
pmNewCfgMonitoredTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgMonitoredTraffic.setStatus(_L)
class _PmCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_PmCurCfgState_Type.__name__=_C
_PmCurCfgState_Object=MibScalar
pmCurCfgState=_PmCurCfgState_Object((1,3,6,1,4,1,1872,2,1,6,7),_PmCurCfgState_Type())
pmCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgState.setStatus(_L)
class _PmNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_F,3)))
_PmNewCfgState_Type.__name__=_C
_PmNewCfgState_Object=MibScalar
pmNewCfgState=_PmNewCfgState_Object((1,3,6,1,4,1,1872,2,1,6,8),_PmNewCfgState_Type())
pmNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgState.setStatus(_L)
class _PmCurCfgTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_PmCurCfgTimeout_Type.__name__=_C
_PmCurCfgTimeout_Object=MibScalar
pmCurCfgTimeout=_PmCurCfgTimeout_Object((1,3,6,1,4,1,1872,2,1,6,9),_PmCurCfgTimeout_Type())
pmCurCfgTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgTimeout.setStatus(_L)
class _PmNewCfgTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_PmNewCfgTimeout_Type.__name__=_C
_PmNewCfgTimeout_Object=MibScalar
pmNewCfgTimeout=_PmNewCfgTimeout_Object((1,3,6,1,4,1,1872,2,1,6,10),_PmNewCfgTimeout_Type())
pmNewCfgTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgTimeout.setStatus(_L)
_Trunkgroup_ObjectIdentity=ObjectIdentity
trunkgroup=_Trunkgroup_ObjectIdentity((1,3,6,1,4,1,1872,2,1,7))
_TrunkGroupTableMaxSize_Type=Integer32
_TrunkGroupTableMaxSize_Object=MibScalar
trunkGroupTableMaxSize=_TrunkGroupTableMaxSize_Object((1,3,6,1,4,1,1872,2,1,7,1),_TrunkGroupTableMaxSize_Type())
trunkGroupTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupTableMaxSize.setStatus(_A)
_TrunkGroupCurCfgTable_Object=MibTable
trunkGroupCurCfgTable=_TrunkGroupCurCfgTable_Object((1,3,6,1,4,1,1872,2,1,7,2))
if mibBuilder.loadTexts:trunkGroupCurCfgTable.setStatus(_A)
_TrunkGroupCurCfgTableEntry_Object=MibTableRow
trunkGroupCurCfgTableEntry=_TrunkGroupCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,7,2,1))
trunkGroupCurCfgTableEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:trunkGroupCurCfgTableEntry.setStatus(_A)
_TrunkGroupCurCfgIndex_Type=Integer32
_TrunkGroupCurCfgIndex_Object=MibTableColumn
trunkGroupCurCfgIndex=_TrunkGroupCurCfgIndex_Object((1,3,6,1,4,1,1872,2,1,7,2,1,1),_TrunkGroupCurCfgIndex_Type())
trunkGroupCurCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgIndex.setStatus(_A)
class _TrunkGroupCurCfgPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TrunkGroupCurCfgPorts_Type.__name__=_M
_TrunkGroupCurCfgPorts_Object=MibTableColumn
trunkGroupCurCfgPorts=_TrunkGroupCurCfgPorts_Object((1,3,6,1,4,1,1872,2,1,7,2,1,2),_TrunkGroupCurCfgPorts_Type())
trunkGroupCurCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgPorts.setStatus(_A)
class _TrunkGroupCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_TrunkGroupCurCfgState_Type.__name__=_C
_TrunkGroupCurCfgState_Object=MibTableColumn
trunkGroupCurCfgState=_TrunkGroupCurCfgState_Object((1,3,6,1,4,1,1872,2,1,7,2,1,3),_TrunkGroupCurCfgState_Type())
trunkGroupCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgState.setStatus(_A)
_TrunkGroupCurCfgBwmContract_Type=Integer32
_TrunkGroupCurCfgBwmContract_Object=MibTableColumn
trunkGroupCurCfgBwmContract=_TrunkGroupCurCfgBwmContract_Object((1,3,6,1,4,1,1872,2,1,7,2,1,4),_TrunkGroupCurCfgBwmContract_Type())
trunkGroupCurCfgBwmContract.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupCurCfgBwmContract.setStatus(_A)
_TrunkGroupNewCfgTable_Object=MibTable
trunkGroupNewCfgTable=_TrunkGroupNewCfgTable_Object((1,3,6,1,4,1,1872,2,1,7,3))
if mibBuilder.loadTexts:trunkGroupNewCfgTable.setStatus(_A)
_TrunkGroupNewCfgTableEntry_Object=MibTableRow
trunkGroupNewCfgTableEntry=_TrunkGroupNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,7,3,1))
trunkGroupNewCfgTableEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:trunkGroupNewCfgTableEntry.setStatus(_A)
_TrunkGroupNewCfgIndex_Type=Integer32
_TrunkGroupNewCfgIndex_Object=MibTableColumn
trunkGroupNewCfgIndex=_TrunkGroupNewCfgIndex_Object((1,3,6,1,4,1,1872,2,1,7,3,1,1),_TrunkGroupNewCfgIndex_Type())
trunkGroupNewCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupNewCfgIndex.setStatus(_A)
class _TrunkGroupNewCfgPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TrunkGroupNewCfgPorts_Type.__name__=_M
_TrunkGroupNewCfgPorts_Object=MibTableColumn
trunkGroupNewCfgPorts=_TrunkGroupNewCfgPorts_Object((1,3,6,1,4,1,1872,2,1,7,3,1,2),_TrunkGroupNewCfgPorts_Type())
trunkGroupNewCfgPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkGroupNewCfgPorts.setStatus(_A)
_TrunkGroupNewCfgAddPort_Type=Integer32
_TrunkGroupNewCfgAddPort_Object=MibTableColumn
trunkGroupNewCfgAddPort=_TrunkGroupNewCfgAddPort_Object((1,3,6,1,4,1,1872,2,1,7,3,1,3),_TrunkGroupNewCfgAddPort_Type())
trunkGroupNewCfgAddPort.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgAddPort.setStatus(_A)
_TrunkGroupNewCfgRemovePort_Type=Integer32
_TrunkGroupNewCfgRemovePort_Object=MibTableColumn
trunkGroupNewCfgRemovePort=_TrunkGroupNewCfgRemovePort_Object((1,3,6,1,4,1,1872,2,1,7,3,1,4),_TrunkGroupNewCfgRemovePort_Type())
trunkGroupNewCfgRemovePort.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgRemovePort.setStatus(_A)
class _TrunkGroupNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_TrunkGroupNewCfgState_Type.__name__=_C
_TrunkGroupNewCfgState_Object=MibTableColumn
trunkGroupNewCfgState=_TrunkGroupNewCfgState_Object((1,3,6,1,4,1,1872,2,1,7,3,1,5),_TrunkGroupNewCfgState_Type())
trunkGroupNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgState.setStatus(_A)
class _TrunkGroupNewCfgDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_V,2)))
_TrunkGroupNewCfgDelete_Type.__name__=_C
_TrunkGroupNewCfgDelete_Object=MibTableColumn
trunkGroupNewCfgDelete=_TrunkGroupNewCfgDelete_Object((1,3,6,1,4,1,1872,2,1,7,3,1,6),_TrunkGroupNewCfgDelete_Type())
trunkGroupNewCfgDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgDelete.setStatus(_A)
_TrunkGroupNewCfgBwmContract_Type=Integer32
_TrunkGroupNewCfgBwmContract_Object=MibTableColumn
trunkGroupNewCfgBwmContract=_TrunkGroupNewCfgBwmContract_Object((1,3,6,1,4,1,1872,2,1,7,3,1,7),_TrunkGroupNewCfgBwmContract_Type())
trunkGroupNewCfgBwmContract.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkGroupNewCfgBwmContract.setStatus(_A)
_PortCpuStats_ObjectIdentity=ObjectIdentity
portCpuStats=_PortCpuStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,17))
_PortCpuStatsUtilTable_Object=MibTable
portCpuStatsUtilTable=_PortCpuStatsUtilTable_Object((1,3,6,1,4,1,1872,2,1,8,17,1))
if mibBuilder.loadTexts:portCpuStatsUtilTable.setStatus(_A)
_PortCpuStatsUtilTableEntry_Object=MibTableRow
portCpuStatsUtilTableEntry=_PortCpuStatsUtilTableEntry_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1))
portCpuStatsUtilTableEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:portCpuStatsUtilTableEntry.setStatus(_A)
class _PortCpuStatsUtilIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortCpuStatsUtilIndx_Type.__name__=_C
_PortCpuStatsUtilIndx_Object=MibTableColumn
portCpuStatsUtilIndx=_PortCpuStatsUtilIndx_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1,1),_PortCpuStatsUtilIndx_Type())
portCpuStatsUtilIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:portCpuStatsUtilIndx.setStatus(_A)
_PortCpuAStatsUtil1Second_Type=Integer32
_PortCpuAStatsUtil1Second_Object=MibTableColumn
portCpuAStatsUtil1Second=_PortCpuAStatsUtil1Second_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1,2),_PortCpuAStatsUtil1Second_Type())
portCpuAStatsUtil1Second.setMaxAccess(_B)
if mibBuilder.loadTexts:portCpuAStatsUtil1Second.setStatus(_A)
_PortCpuBStatsUtil1Second_Type=Integer32
_PortCpuBStatsUtil1Second_Object=MibTableColumn
portCpuBStatsUtil1Second=_PortCpuBStatsUtil1Second_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1,3),_PortCpuBStatsUtil1Second_Type())
portCpuBStatsUtil1Second.setMaxAccess(_B)
if mibBuilder.loadTexts:portCpuBStatsUtil1Second.setStatus(_A)
_PortCpuAStatsUtil4Seconds_Type=Integer32
_PortCpuAStatsUtil4Seconds_Object=MibTableColumn
portCpuAStatsUtil4Seconds=_PortCpuAStatsUtil4Seconds_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1,4),_PortCpuAStatsUtil4Seconds_Type())
portCpuAStatsUtil4Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:portCpuAStatsUtil4Seconds.setStatus(_A)
_PortCpuBStatsUtil4Seconds_Type=Integer32
_PortCpuBStatsUtil4Seconds_Object=MibTableColumn
portCpuBStatsUtil4Seconds=_PortCpuBStatsUtil4Seconds_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1,5),_PortCpuBStatsUtil4Seconds_Type())
portCpuBStatsUtil4Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:portCpuBStatsUtil4Seconds.setStatus(_A)
_PortCpuAStatsUtil64Seconds_Type=Integer32
_PortCpuAStatsUtil64Seconds_Object=MibTableColumn
portCpuAStatsUtil64Seconds=_PortCpuAStatsUtil64Seconds_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1,6),_PortCpuAStatsUtil64Seconds_Type())
portCpuAStatsUtil64Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:portCpuAStatsUtil64Seconds.setStatus(_A)
_PortCpuBStatsUtil64Seconds_Type=Integer32
_PortCpuBStatsUtil64Seconds_Object=MibTableColumn
portCpuBStatsUtil64Seconds=_PortCpuBStatsUtil64Seconds_Object((1,3,6,1,4,1,1872,2,1,8,17,1,1,7),_PortCpuBStatsUtil64Seconds_Type())
portCpuBStatsUtil64Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:portCpuBStatsUtil64Seconds.setStatus(_A)
_Port_stats_ObjectIdentity=ObjectIdentity
port_stats=_Port_stats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,26))
_PortStatsTable_Object=MibTable
portStatsTable=_PortStatsTable_Object((1,3,6,1,4,1,1872,2,1,8,26,1))
if mibBuilder.loadTexts:portStatsTable.setStatus(_A)
_PortStatsTableEntry_Object=MibTableRow
portStatsTableEntry=_PortStatsTableEntry_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1))
portStatsTableEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:portStatsTableEntry.setStatus(_A)
class _PortStatsIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortStatsIndx_Type.__name__=_C
_PortStatsIndx_Object=MibTableColumn
portStatsIndx=_PortStatsIndx_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,1),_PortStatsIndx_Type())
portStatsIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsIndx.setStatus(_A)
_PortStatsPhyIfInOctets_Type=Counter32
_PortStatsPhyIfInOctets_Object=MibTableColumn
portStatsPhyIfInOctets=_PortStatsPhyIfInOctets_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,2),_PortStatsPhyIfInOctets_Type())
portStatsPhyIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfInOctets.setStatus(_A)
_PortStatsPhyIfInUcastPkts_Type=Counter32
_PortStatsPhyIfInUcastPkts_Object=MibTableColumn
portStatsPhyIfInUcastPkts=_PortStatsPhyIfInUcastPkts_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,3),_PortStatsPhyIfInUcastPkts_Type())
portStatsPhyIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfInUcastPkts.setStatus(_A)
_PortStatsPhyIfInNUcastPkts_Type=Counter32
_PortStatsPhyIfInNUcastPkts_Object=MibTableColumn
portStatsPhyIfInNUcastPkts=_PortStatsPhyIfInNUcastPkts_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,4),_PortStatsPhyIfInNUcastPkts_Type())
portStatsPhyIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfInNUcastPkts.setStatus(_A)
_PortStatsPhyIfInDiscards_Type=Counter32
_PortStatsPhyIfInDiscards_Object=MibTableColumn
portStatsPhyIfInDiscards=_PortStatsPhyIfInDiscards_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,5),_PortStatsPhyIfInDiscards_Type())
portStatsPhyIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfInDiscards.setStatus(_A)
_PortStatsPhyIfInErrors_Type=Counter32
_PortStatsPhyIfInErrors_Object=MibTableColumn
portStatsPhyIfInErrors=_PortStatsPhyIfInErrors_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,6),_PortStatsPhyIfInErrors_Type())
portStatsPhyIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfInErrors.setStatus(_A)
_PortStatsPhyIfInUnknownProtos_Type=Counter32
_PortStatsPhyIfInUnknownProtos_Object=MibTableColumn
portStatsPhyIfInUnknownProtos=_PortStatsPhyIfInUnknownProtos_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,7),_PortStatsPhyIfInUnknownProtos_Type())
portStatsPhyIfInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfInUnknownProtos.setStatus(_A)
_PortStatsPhyIfOutOctets_Type=Counter32
_PortStatsPhyIfOutOctets_Object=MibTableColumn
portStatsPhyIfOutOctets=_PortStatsPhyIfOutOctets_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,8),_PortStatsPhyIfOutOctets_Type())
portStatsPhyIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfOutOctets.setStatus(_A)
_PortStatsPhyIfOutUcastPkts_Type=Counter32
_PortStatsPhyIfOutUcastPkts_Object=MibTableColumn
portStatsPhyIfOutUcastPkts=_PortStatsPhyIfOutUcastPkts_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,9),_PortStatsPhyIfOutUcastPkts_Type())
portStatsPhyIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfOutUcastPkts.setStatus(_A)
_PortStatsPhyIfOutNUcastPkts_Type=Counter32
_PortStatsPhyIfOutNUcastPkts_Object=MibTableColumn
portStatsPhyIfOutNUcastPkts=_PortStatsPhyIfOutNUcastPkts_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,10),_PortStatsPhyIfOutNUcastPkts_Type())
portStatsPhyIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfOutNUcastPkts.setStatus(_A)
_PortStatsPhyIfOutDiscards_Type=Counter32
_PortStatsPhyIfOutDiscards_Object=MibTableColumn
portStatsPhyIfOutDiscards=_PortStatsPhyIfOutDiscards_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,11),_PortStatsPhyIfOutDiscards_Type())
portStatsPhyIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfOutDiscards.setStatus(_A)
_PortStatsPhyIfOutErrors_Type=Counter32
_PortStatsPhyIfOutErrors_Object=MibTableColumn
portStatsPhyIfOutErrors=_PortStatsPhyIfOutErrors_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,12),_PortStatsPhyIfOutErrors_Type())
portStatsPhyIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfOutErrors.setStatus(_A)
_PortStatsPhyIfOutQLen_Type=Gauge32
_PortStatsPhyIfOutQLen_Object=MibTableColumn
portStatsPhyIfOutQLen=_PortStatsPhyIfOutQLen_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,13),_PortStatsPhyIfOutQLen_Type())
portStatsPhyIfOutQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfOutQLen.setStatus(_A)
_PortStatsPhyIfInBroadcastPkts_Type=Counter32
_PortStatsPhyIfInBroadcastPkts_Object=MibTableColumn
portStatsPhyIfInBroadcastPkts=_PortStatsPhyIfInBroadcastPkts_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,14),_PortStatsPhyIfInBroadcastPkts_Type())
portStatsPhyIfInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfInBroadcastPkts.setStatus(_A)
_PortStatsPhyIfOutBroadcastPkts_Type=Counter32
_PortStatsPhyIfOutBroadcastPkts_Object=MibTableColumn
portStatsPhyIfOutBroadcastPkts=_PortStatsPhyIfOutBroadcastPkts_Object((1,3,6,1,4,1,1872,2,1,8,26,1,1,15),_PortStatsPhyIfOutBroadcastPkts_Type())
portStatsPhyIfOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:portStatsPhyIfOutBroadcastPkts.setStatus(_A)
_Port_info_ObjectIdentity=ObjectIdentity
port_info=_Port_info_ObjectIdentity((1,3,6,1,4,1,1872,2,1,9,1))
_PortInfoTable_Object=MibTable
portInfoTable=_PortInfoTable_Object((1,3,6,1,4,1,1872,2,1,9,1,1))
if mibBuilder.loadTexts:portInfoTable.setStatus(_A)
_PortInfoTableEntry_Object=MibTableRow
portInfoTableEntry=_PortInfoTableEntry_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1))
portInfoTableEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:portInfoTableEntry.setStatus(_A)
class _PortInfoIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortInfoIndx_Type.__name__=_C
_PortInfoIndx_Object=MibTableColumn
portInfoIndx=_PortInfoIndx_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,1),_PortInfoIndx_Type())
portInfoIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoIndx.setStatus(_A)
class _PortInfoSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_W,2),(_X,3),('mbs1000',4),('any',5)))
_PortInfoSpeed_Type.__name__=_C
_PortInfoSpeed_Object=MibTableColumn
portInfoSpeed=_PortInfoSpeed_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,2),_PortInfoSpeed_Type())
portInfoSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoSpeed.setStatus(_A)
class _PortInfoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Y,2),(_Z,3)))
_PortInfoMode_Type.__name__=_C
_PortInfoMode_Object=MibTableColumn
portInfoMode=_PortInfoMode_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,3),_PortInfoMode_Type())
portInfoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoMode.setStatus(_A)
class _PortInfoFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_O,2),(_P,3),(_J,4),(_K,5)))
_PortInfoFlowCtrl_Type.__name__=_C
_PortInfoFlowCtrl_Object=MibTableColumn
portInfoFlowCtrl=_PortInfoFlowCtrl_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,4),_PortInfoFlowCtrl_Type())
portInfoFlowCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoFlowCtrl.setStatus(_A)
class _PortInfoLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),(_F,3),('inoperative',4)))
_PortInfoLink_Type.__name__=_C
_PortInfoLink_Object=MibTableColumn
portInfoLink=_PortInfoLink_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,5),_PortInfoLink_Type())
portInfoLink.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoLink.setStatus(_A)
class _PortInfoPhyIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PortInfoPhyIfDescr_Type.__name__=_N
_PortInfoPhyIfDescr_Object=MibTableColumn
portInfoPhyIfDescr=_PortInfoPhyIfDescr_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,6),_PortInfoPhyIfDescr_Type())
portInfoPhyIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoPhyIfDescr.setStatus(_A)
class _PortInfoPhyIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)));namedValues=NamedValues(*((_Q,1),('regular1822',2),('hdh1822',3),('ddn-x25',4),('rfc877-x25',5),('ethernet-csmacd',6),('iso88023-csmacd',7),('iso88024-tokenBus',8),('iso88025-tokenRing',9),('iso88026-man',10),('starLan',11),('proteon-10Mbit',12),('proteon-80Mbit',13),('hyperchannel',14),('fddi',15),('lapb',16),('sdlc',17),('ds1',18),('e1',19),('basicISDN',20),('primaryISDN',21),('propPointToPointSerial',22),('ppp',23),('softwareLoopback',24),('eon',25),('ethernet-3Mbit',26),('nsip',27),('slip',28),('ultra',29),('ds3',30),('sip',31),('frame-relay',32)))
_PortInfoPhyIfType_Type.__name__=_C
_PortInfoPhyIfType_Object=MibTableColumn
portInfoPhyIfType=_PortInfoPhyIfType_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,7),_PortInfoPhyIfType_Type())
portInfoPhyIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoPhyIfType.setStatus(_A)
_PortInfoPhyIfMtu_Type=Integer32
_PortInfoPhyIfMtu_Object=MibTableColumn
portInfoPhyIfMtu=_PortInfoPhyIfMtu_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,8),_PortInfoPhyIfMtu_Type())
portInfoPhyIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoPhyIfMtu.setStatus(_A)
_PortInfoPhyIfPhysAddress_Type=PhysAddress
_PortInfoPhyIfPhysAddress_Object=MibTableColumn
portInfoPhyIfPhysAddress=_PortInfoPhyIfPhysAddress_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,9),_PortInfoPhyIfPhysAddress_Type())
portInfoPhyIfPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoPhyIfPhysAddress.setStatus(_A)
class _PortInfoPhyIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_PortInfoPhyIfOperStatus_Type.__name__=_C
_PortInfoPhyIfOperStatus_Object=MibTableColumn
portInfoPhyIfOperStatus=_PortInfoPhyIfOperStatus_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,10),_PortInfoPhyIfOperStatus_Type())
portInfoPhyIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoPhyIfOperStatus.setStatus(_A)
_PortInfoPhyIfLastChange_Type=TimeTicks
_PortInfoPhyIfLastChange_Object=MibTableColumn
portInfoPhyIfLastChange=_PortInfoPhyIfLastChange_Object((1,3,6,1,4,1,1872,2,1,9,1,1,1,11),_PortInfoPhyIfLastChange_Type())
portInfoPhyIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:portInfoPhyIfLastChange.setStatus(_A)
_MirrOper_ObjectIdentity=ObjectIdentity
mirrOper=_MirrOper_ObjectIdentity((1,3,6,1,4,1,1872,2,1,14,3))
_MirrOperMonitoringPort_Type=Integer32
_MirrOperMonitoringPort_Object=MibScalar
mirrOperMonitoringPort=_MirrOperMonitoringPort_Object((1,3,6,1,4,1,1872,2,1,14,3,1),_MirrOperMonitoringPort_Type())
mirrOperMonitoringPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrOperMonitoringPort.setStatus(_A)
_MirrOperMirroredPort_Type=Integer32
_MirrOperMirroredPort_Object=MibScalar
mirrOperMirroredPort=_MirrOperMirroredPort_Object((1,3,6,1,4,1,1872,2,1,14,3,2),_MirrOperMirroredPort_Type())
mirrOperMirroredPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrOperMirroredPort.setStatus(_A)
class _MirrOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_R,2),(_S,3),(_J,4)))
_MirrOperType_Type.__name__=_C
_MirrOperType_Object=MibScalar
mirrOperType=_MirrOperType_Object((1,3,6,1,4,1,1872,2,1,14,3,3),_MirrOperType_Type())
mirrOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrOperType.setStatus(_A)
class _MirrOperTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_MirrOperTimeout_Type.__name__=_C
_MirrOperTimeout_Object=MibScalar
mirrOperTimeout=_MirrOperTimeout_Object((1,3,6,1,4,1,1872,2,1,14,3,4),_MirrOperTimeout_Type())
mirrOperTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrOperTimeout.setStatus(_A)
class _MirrOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_MirrOperState_Type.__name__=_C
_MirrOperState_Object=MibScalar
mirrOperState=_MirrOperState_Object((1,3,6,1,4,1,1872,2,1,14,3,5),_MirrOperState_Type())
mirrOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:mirrOperState.setStatus(_A)
_Mirroring_ObjectIdentity=ObjectIdentity
mirroring=_Mirroring_ObjectIdentity((1,3,6,1,4,1,1872,2,1,18))
_MirrPortMirr_ObjectIdentity=ObjectIdentity
mirrPortMirr=_MirrPortMirr_ObjectIdentity((1,3,6,1,4,1,1872,2,1,18,1))
class _PmCurCfgPortMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_PmCurCfgPortMirrState_Type.__name__=_C
_PmCurCfgPortMirrState_Object=MibScalar
pmCurCfgPortMirrState=_PmCurCfgPortMirrState_Object((1,3,6,1,4,1,1872,2,1,18,1,1),_PmCurCfgPortMirrState_Type())
pmCurCfgPortMirrState.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPortMirrState.setStatus(_A)
class _PmNewCfgPortMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_PmNewCfgPortMirrState_Type.__name__=_C
_PmNewCfgPortMirrState_Object=MibScalar
pmNewCfgPortMirrState=_PmNewCfgPortMirrState_Object((1,3,6,1,4,1,1872,2,1,18,1,2),_PmNewCfgPortMirrState_Type())
pmNewCfgPortMirrState.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPortMirrState.setStatus(_A)
_PmCurCfgPortMonitorTable_Object=MibTable
pmCurCfgPortMonitorTable=_PmCurCfgPortMonitorTable_Object((1,3,6,1,4,1,1872,2,1,18,1,3))
if mibBuilder.loadTexts:pmCurCfgPortMonitorTable.setStatus(_A)
_PmCurCfgPortMonitorEntry_Object=MibTableRow
pmCurCfgPortMonitorEntry=_PmCurCfgPortMonitorEntry_Object((1,3,6,1,4,1,1872,2,1,18,1,3,1))
pmCurCfgPortMonitorEntry.setIndexNames((0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:pmCurCfgPortMonitorEntry.setStatus(_A)
_PmCurCfgPmirrMoniPortIndex_Type=Integer32
_PmCurCfgPmirrMoniPortIndex_Object=MibTableColumn
pmCurCfgPmirrMoniPortIndex=_PmCurCfgPmirrMoniPortIndex_Object((1,3,6,1,4,1,1872,2,1,18,1,3,1,1),_PmCurCfgPmirrMoniPortIndex_Type())
pmCurCfgPmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrMoniPortIndex.setStatus(_A)
_PmCurCfgPmirrMirrPortIndex_Type=Integer32
_PmCurCfgPmirrMirrPortIndex_Object=MibTableColumn
pmCurCfgPmirrMirrPortIndex=_PmCurCfgPmirrMirrPortIndex_Object((1,3,6,1,4,1,1872,2,1,18,1,3,1,2),_PmCurCfgPmirrMirrPortIndex_Type())
pmCurCfgPmirrMirrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrMirrPortIndex.setStatus(_A)
class _PmCurCfgPmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_J,3)))
_PmCurCfgPmirrDirection_Type.__name__=_C
_PmCurCfgPmirrDirection_Object=MibTableColumn
pmCurCfgPmirrDirection=_PmCurCfgPmirrDirection_Object((1,3,6,1,4,1,1872,2,1,18,1,3,1,3),_PmCurCfgPmirrDirection_Type())
pmCurCfgPmirrDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgPmirrDirection.setStatus(_A)
_PmNewCfgPortMonitorTable_Object=MibTable
pmNewCfgPortMonitorTable=_PmNewCfgPortMonitorTable_Object((1,3,6,1,4,1,1872,2,1,18,1,4))
if mibBuilder.loadTexts:pmNewCfgPortMonitorTable.setStatus(_A)
_PmNewCfgPortMonitorEntry_Object=MibTableRow
pmNewCfgPortMonitorEntry=_PmNewCfgPortMonitorEntry_Object((1,3,6,1,4,1,1872,2,1,18,1,4,1))
pmNewCfgPortMonitorEntry.setIndexNames((0,_E,_t),(0,_E,_u))
if mibBuilder.loadTexts:pmNewCfgPortMonitorEntry.setStatus(_A)
_PmNewCfgPmirrMoniPortIndex_Type=Integer32
_PmNewCfgPmirrMoniPortIndex_Object=MibTableColumn
pmNewCfgPmirrMoniPortIndex=_PmNewCfgPmirrMoniPortIndex_Object((1,3,6,1,4,1,1872,2,1,18,1,4,1,1),_PmNewCfgPmirrMoniPortIndex_Type())
pmNewCfgPmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgPmirrMoniPortIndex.setStatus(_A)
_PmNewCfgPmirrMirrPortIndex_Type=Integer32
_PmNewCfgPmirrMirrPortIndex_Object=MibTableColumn
pmNewCfgPmirrMirrPortIndex=_PmNewCfgPmirrMirrPortIndex_Object((1,3,6,1,4,1,1872,2,1,18,1,4,1,2),_PmNewCfgPmirrMirrPortIndex_Type())
pmNewCfgPmirrMirrPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgPmirrMirrPortIndex.setStatus(_A)
class _PmNewCfgPmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_J,3)))
_PmNewCfgPmirrDirection_Type.__name__=_C
_PmNewCfgPmirrDirection_Object=MibTableColumn
pmNewCfgPmirrDirection=_PmNewCfgPmirrDirection_Object((1,3,6,1,4,1,1872,2,1,18,1,4,1,3),_PmNewCfgPmirrDirection_Type())
pmNewCfgPmirrDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPmirrDirection.setStatus(_A)
class _PmNewCfgPmirrDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_V,2)))
_PmNewCfgPmirrDelete_Type.__name__=_C
_PmNewCfgPmirrDelete_Object=MibTableColumn
pmNewCfgPmirrDelete=_PmNewCfgPmirrDelete_Object((1,3,6,1,4,1,1872,2,1,18,1,4,1,4),_PmNewCfgPmirrDelete_Type())
pmNewCfgPmirrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgPmirrDelete.setStatus(_A)
_MirrVlanMirr_ObjectIdentity=ObjectIdentity
mirrVlanMirr=_MirrVlanMirr_ObjectIdentity((1,3,6,1,4,1,1872,2,1,18,2))
class _PmCurCfgVlanMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_PmCurCfgVlanMirrState_Type.__name__=_C
_PmCurCfgVlanMirrState_Object=MibScalar
pmCurCfgVlanMirrState=_PmCurCfgVlanMirrState_Object((1,3,6,1,4,1,1872,2,1,18,2,1),_PmCurCfgVlanMirrState_Type())
pmCurCfgVlanMirrState.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgVlanMirrState.setStatus(_A)
class _PmNewCfgVlanMirrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_PmNewCfgVlanMirrState_Type.__name__=_C
_PmNewCfgVlanMirrState_Object=MibScalar
pmNewCfgVlanMirrState=_PmNewCfgVlanMirrState_Object((1,3,6,1,4,1,1872,2,1,18,2,2),_PmNewCfgVlanMirrState_Type())
pmNewCfgVlanMirrState.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgVlanMirrState.setStatus(_A)
_PmCurCfgVlanMonitorTable_Object=MibTable
pmCurCfgVlanMonitorTable=_PmCurCfgVlanMonitorTable_Object((1,3,6,1,4,1,1872,2,1,18,2,3))
if mibBuilder.loadTexts:pmCurCfgVlanMonitorTable.setStatus(_A)
_PmCurCfgVlanMonitorEntry_Object=MibTableRow
pmCurCfgVlanMonitorEntry=_PmCurCfgVlanMonitorEntry_Object((1,3,6,1,4,1,1872,2,1,18,2,3,1))
pmCurCfgVlanMonitorEntry.setIndexNames((0,_E,_v),(0,_E,_w))
if mibBuilder.loadTexts:pmCurCfgVlanMonitorEntry.setStatus(_A)
_PmCurCfgVmirrMoniPortIndex_Type=Integer32
_PmCurCfgVmirrMoniPortIndex_Object=MibTableColumn
pmCurCfgVmirrMoniPortIndex=_PmCurCfgVmirrMoniPortIndex_Object((1,3,6,1,4,1,1872,2,1,18,2,3,1,1),_PmCurCfgVmirrMoniPortIndex_Type())
pmCurCfgVmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgVmirrMoniPortIndex.setStatus(_A)
_PmCurCfgVmirrMirrVlanIndex_Type=Integer32
_PmCurCfgVmirrMirrVlanIndex_Object=MibTableColumn
pmCurCfgVmirrMirrVlanIndex=_PmCurCfgVmirrMirrVlanIndex_Object((1,3,6,1,4,1,1872,2,1,18,2,3,1,2),_PmCurCfgVmirrMirrVlanIndex_Type())
pmCurCfgVmirrMirrVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgVmirrMirrVlanIndex.setStatus(_A)
class _PmCurCfgVmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_J,3)))
_PmCurCfgVmirrDirection_Type.__name__=_C
_PmCurCfgVmirrDirection_Object=MibTableColumn
pmCurCfgVmirrDirection=_PmCurCfgVmirrDirection_Object((1,3,6,1,4,1,1872,2,1,18,2,3,1,3),_PmCurCfgVmirrDirection_Type())
pmCurCfgVmirrDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmCurCfgVmirrDirection.setStatus(_A)
_PmNewCfgVlanMonitorTable_Object=MibTable
pmNewCfgVlanMonitorTable=_PmNewCfgVlanMonitorTable_Object((1,3,6,1,4,1,1872,2,1,18,2,4))
if mibBuilder.loadTexts:pmNewCfgVlanMonitorTable.setStatus(_A)
_PmNewCfgVlanMonitorEntry_Object=MibTableRow
pmNewCfgVlanMonitorEntry=_PmNewCfgVlanMonitorEntry_Object((1,3,6,1,4,1,1872,2,1,18,2,4,1))
pmNewCfgVlanMonitorEntry.setIndexNames((0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:pmNewCfgVlanMonitorEntry.setStatus(_A)
_PmNewCfgVmirrMoniPortIndex_Type=Integer32
_PmNewCfgVmirrMoniPortIndex_Object=MibTableColumn
pmNewCfgVmirrMoniPortIndex=_PmNewCfgVmirrMoniPortIndex_Object((1,3,6,1,4,1,1872,2,1,18,2,4,1,1),_PmNewCfgVmirrMoniPortIndex_Type())
pmNewCfgVmirrMoniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgVmirrMoniPortIndex.setStatus(_A)
_PmNewCfgVmirrMirrVlanIndex_Type=Integer32
_PmNewCfgVmirrMirrVlanIndex_Object=MibTableColumn
pmNewCfgVmirrMirrVlanIndex=_PmNewCfgVmirrMirrVlanIndex_Object((1,3,6,1,4,1,1872,2,1,18,2,4,1,2),_PmNewCfgVmirrMirrVlanIndex_Type())
pmNewCfgVmirrMirrVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmNewCfgVmirrMirrVlanIndex.setStatus(_A)
class _PmNewCfgVmirrDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_J,3)))
_PmNewCfgVmirrDirection_Type.__name__=_C
_PmNewCfgVmirrDirection_Object=MibTableColumn
pmNewCfgVmirrDirection=_PmNewCfgVmirrDirection_Object((1,3,6,1,4,1,1872,2,1,18,2,4,1,3),_PmNewCfgVmirrDirection_Type())
pmNewCfgVmirrDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgVmirrDirection.setStatus(_A)
class _PmNewCfgVmirrDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_V,2)))
_PmNewCfgVmirrDelete_Type.__name__=_C
_PmNewCfgVmirrDelete_Object=MibTableColumn
pmNewCfgVmirrDelete=_PmNewCfgVmirrDelete_Object((1,3,6,1,4,1,1872,2,1,18,2,4,1,4),_PmNewCfgVmirrDelete_Type())
pmNewCfgVmirrDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:pmNewCfgVmirrDelete.setStatus(_A)
_SpannTreeGrpCfg_ObjectIdentity=ObjectIdentity
spannTreeGrpCfg=_SpannTreeGrpCfg_ObjectIdentity((1,3,6,1,4,1,1872,2,1,19))
_StgCurCfgTable_Object=MibTable
stgCurCfgTable=_StgCurCfgTable_Object((1,3,6,1,4,1,1872,2,1,19,1))
if mibBuilder.loadTexts:stgCurCfgTable.setStatus(_A)
_StgCurCfgTableEntry_Object=MibTableRow
stgCurCfgTableEntry=_StgCurCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,19,1,1))
stgCurCfgTableEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:stgCurCfgTableEntry.setStatus(_A)
class _StgCurCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_StgCurCfgIndex_Type.__name__=_C
_StgCurCfgIndex_Object=MibTableColumn
stgCurCfgIndex=_StgCurCfgIndex_Object((1,3,6,1,4,1,1872,2,1,19,1,1,1),_StgCurCfgIndex_Type())
stgCurCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgIndex.setStatus(_A)
class _StgCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_StgCurCfgState_Type.__name__=_C
_StgCurCfgState_Object=MibTableColumn
stgCurCfgState=_StgCurCfgState_Object((1,3,6,1,4,1,1872,2,1,19,1,1,2),_StgCurCfgState_Type())
stgCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgState.setStatus(_A)
class _StgCurCfgVlanBmap1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgCurCfgVlanBmap1_Type.__name__=_M
_StgCurCfgVlanBmap1_Object=MibTableColumn
stgCurCfgVlanBmap1=_StgCurCfgVlanBmap1_Object((1,3,6,1,4,1,1872,2,1,19,1,1,3),_StgCurCfgVlanBmap1_Type())
stgCurCfgVlanBmap1.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgVlanBmap1.setStatus(_A)
class _StgCurCfgVlanBmap2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgCurCfgVlanBmap2_Type.__name__=_M
_StgCurCfgVlanBmap2_Object=MibTableColumn
stgCurCfgVlanBmap2=_StgCurCfgVlanBmap2_Object((1,3,6,1,4,1,1872,2,1,19,1,1,4),_StgCurCfgVlanBmap2_Type())
stgCurCfgVlanBmap2.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgVlanBmap2.setStatus(_A)
_StgNewCfgTable_Object=MibTable
stgNewCfgTable=_StgNewCfgTable_Object((1,3,6,1,4,1,1872,2,1,19,2))
if mibBuilder.loadTexts:stgNewCfgTable.setStatus(_A)
_StgNewCfgTableEntry_Object=MibTableRow
stgNewCfgTableEntry=_StgNewCfgTableEntry_Object((1,3,6,1,4,1,1872,2,1,19,2,1))
stgNewCfgTableEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:stgNewCfgTableEntry.setStatus(_A)
class _StgNewCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_StgNewCfgIndex_Type.__name__=_C
_StgNewCfgIndex_Object=MibTableColumn
stgNewCfgIndex=_StgNewCfgIndex_Object((1,3,6,1,4,1,1872,2,1,19,2,1,1),_StgNewCfgIndex_Type())
stgNewCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgIndex.setStatus(_A)
class _StgNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_StgNewCfgState_Type.__name__=_C
_StgNewCfgState_Object=MibTableColumn
stgNewCfgState=_StgNewCfgState_Object((1,3,6,1,4,1,1872,2,1,19,2,1,2),_StgNewCfgState_Type())
stgNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgState.setStatus(_A)
class _StgNewCfgDefaultCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('default-config',1))
_StgNewCfgDefaultCfg_Type.__name__=_C
_StgNewCfgDefaultCfg_Object=MibTableColumn
stgNewCfgDefaultCfg=_StgNewCfgDefaultCfg_Object((1,3,6,1,4,1,1872,2,1,19,2,1,3),_StgNewCfgDefaultCfg_Type())
stgNewCfgDefaultCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgDefaultCfg.setStatus(_A)
_StgNewCfgAddVlan_Type=Integer32
_StgNewCfgAddVlan_Object=MibTableColumn
stgNewCfgAddVlan=_StgNewCfgAddVlan_Object((1,3,6,1,4,1,1872,2,1,19,2,1,4),_StgNewCfgAddVlan_Type())
stgNewCfgAddVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgAddVlan.setStatus(_A)
_StgNewCfgRemoveVlan_Type=Integer32
_StgNewCfgRemoveVlan_Object=MibTableColumn
stgNewCfgRemoveVlan=_StgNewCfgRemoveVlan_Object((1,3,6,1,4,1,1872,2,1,19,2,1,5),_StgNewCfgRemoveVlan_Type())
stgNewCfgRemoveVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgRemoveVlan.setStatus(_A)
class _StgNewCfgVlanBmap1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgNewCfgVlanBmap1_Type.__name__=_M
_StgNewCfgVlanBmap1_Object=MibTableColumn
stgNewCfgVlanBmap1=_StgNewCfgVlanBmap1_Object((1,3,6,1,4,1,1872,2,1,19,2,1,6),_StgNewCfgVlanBmap1_Type())
stgNewCfgVlanBmap1.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgVlanBmap1.setStatus(_A)
class _StgNewCfgVlanBmap2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_StgNewCfgVlanBmap2_Type.__name__=_M
_StgNewCfgVlanBmap2_Object=MibTableColumn
stgNewCfgVlanBmap2=_StgNewCfgVlanBmap2_Object((1,3,6,1,4,1,1872,2,1,19,2,1,7),_StgNewCfgVlanBmap2_Type())
stgNewCfgVlanBmap2.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgVlanBmap2.setStatus(_A)
_StgCurCfgPortTable_Object=MibTable
stgCurCfgPortTable=_StgCurCfgPortTable_Object((1,3,6,1,4,1,1872,2,1,19,3))
if mibBuilder.loadTexts:stgCurCfgPortTable.setStatus(_A)
_StgCurCfgPortTableEntry_Object=MibTableRow
stgCurCfgPortTableEntry=_StgCurCfgPortTableEntry_Object((1,3,6,1,4,1,1872,2,1,19,3,1))
stgCurCfgPortTableEntry.setIndexNames((0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:stgCurCfgPortTableEntry.setStatus(_A)
_StgCurCfgStgIndex_Type=Integer32
_StgCurCfgStgIndex_Object=MibTableColumn
stgCurCfgStgIndex=_StgCurCfgStgIndex_Object((1,3,6,1,4,1,1872,2,1,19,3,1,1),_StgCurCfgStgIndex_Type())
stgCurCfgStgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgStgIndex.setStatus(_A)
_StgCurCfgPortIndex_Type=Integer32
_StgCurCfgPortIndex_Object=MibTableColumn
stgCurCfgPortIndex=_StgCurCfgPortIndex_Object((1,3,6,1,4,1,1872,2,1,19,3,1,2),_StgCurCfgPortIndex_Type())
stgCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortIndex.setStatus(_A)
class _StgCurCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_StgCurCfgPortState_Type.__name__=_C
_StgCurCfgPortState_Object=MibTableColumn
stgCurCfgPortState=_StgCurCfgPortState_Object((1,3,6,1,4,1,1872,2,1,19,3,1,3),_StgCurCfgPortState_Type())
stgCurCfgPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:stgCurCfgPortState.setStatus(_A)
_StgNewCfgPortTable_Object=MibTable
stgNewCfgPortTable=_StgNewCfgPortTable_Object((1,3,6,1,4,1,1872,2,1,19,4))
if mibBuilder.loadTexts:stgNewCfgPortTable.setStatus(_A)
_StgNewCfgPortTableEntry_Object=MibTableRow
stgNewCfgPortTableEntry=_StgNewCfgPortTableEntry_Object((1,3,6,1,4,1,1872,2,1,19,4,1))
stgNewCfgPortTableEntry.setIndexNames((0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:stgNewCfgPortTableEntry.setStatus(_A)
_StgNewCfgStgIndex_Type=Integer32
_StgNewCfgStgIndex_Object=MibTableColumn
stgNewCfgStgIndex=_StgNewCfgStgIndex_Object((1,3,6,1,4,1,1872,2,1,19,4,1,1),_StgNewCfgStgIndex_Type())
stgNewCfgStgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgStgIndex.setStatus(_A)
_StgNewCfgPortIndex_Type=Integer32
_StgNewCfgPortIndex_Object=MibTableColumn
stgNewCfgPortIndex=_StgNewCfgPortIndex_Object((1,3,6,1,4,1,1872,2,1,19,4,1,2),_StgNewCfgPortIndex_Type())
stgNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stgNewCfgPortIndex.setStatus(_A)
class _StgNewCfgPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_StgNewCfgPortState_Type.__name__=_C
_StgNewCfgPortState_Object=MibTableColumn
stgNewCfgPortState=_StgNewCfgPortState_Object((1,3,6,1,4,1,1872,2,1,19,4,1,3),_StgNewCfgPortState_Type())
stgNewCfgPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:stgNewCfgPortState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'agPortConfig':agPortConfig,'agPortTableMaxEnt':agPortTableMaxEnt,'agPortCurCfgTable':agPortCurCfgTable,'agPortCurCfgTableEntry':agPortCurCfgTableEntry,_a:agPortCurCfgIndx,'agPortCurCfgPrefLink':agPortCurCfgPrefLink,'agPortCurCfgBackLink':agPortCurCfgBackLink,'agPortCurCfgState':agPortCurCfgState,'agPortCurCfgVlanTag':agPortCurCfgVlanTag,'agPortCurCfgStp':agPortCurCfgStp,'agPortCurCfgRmon':agPortCurCfgRmon,'agPortCurCfgPVID':agPortCurCfgPVID,'agPortCurCfgFastEthAutoNeg':agPortCurCfgFastEthAutoNeg,'agPortCurCfgFastEthSpeed':agPortCurCfgFastEthSpeed,'agPortCurCfgFastEthMode':agPortCurCfgFastEthMode,'agPortCurCfgFastEthFctl':agPortCurCfgFastEthFctl,'agPortCurCfgGigEthAutoNeg':agPortCurCfgGigEthAutoNeg,'agPortCurCfgGigEthFctl':agPortCurCfgGigEthFctl,'agPortCurCfgPortName':agPortCurCfgPortName,'agPortCurCfgBwmContract':agPortCurCfgBwmContract,'agPortCurCfgDiscardNonIPs':agPortCurCfgDiscardNonIPs,'agPortCurCfgLinkTrap':agPortCurCfgLinkTrap,'agPortNewCfgTable':agPortNewCfgTable,'agPortNewCfgTableEntry':agPortNewCfgTableEntry,_f:agPortNewCfgIndx,'agPortNewCfgPrefLink':agPortNewCfgPrefLink,'agPortNewCfgBackLink':agPortNewCfgBackLink,'agPortNewCfgState':agPortNewCfgState,'agPortNewCfgVlanTag':agPortNewCfgVlanTag,'agPortNewCfgStp':agPortNewCfgStp,'agPortNewCfgRmon':agPortNewCfgRmon,'agPortNewCfgPVID':agPortNewCfgPVID,'agPortNewCfgFastEthAutoNeg':agPortNewCfgFastEthAutoNeg,'agPortNewCfgFastEthSpeed':agPortNewCfgFastEthSpeed,'agPortNewCfgFastEthMode':agPortNewCfgFastEthMode,'agPortNewCfgFastEthFctl':agPortNewCfgFastEthFctl,'agPortNewCfgGigEthAutoNeg':agPortNewCfgGigEthAutoNeg,'agPortNewCfgGigEthFctl':agPortNewCfgGigEthFctl,'agPortNewCfgPortName':agPortNewCfgPortName,'agPortNewCfgBwmContract':agPortNewCfgBwmContract,'agPortNewCfgDiscardNonIPs':agPortNewCfgDiscardNonIPs,'agPortNewCfgLinkTrap':agPortNewCfgLinkTrap,'vlans':vlans,'vlanMaxEnt':vlanMaxEnt,'vlanCurCfgTable':vlanCurCfgTable,'vlanCurCfgTableEntry':vlanCurCfgTableEntry,_g:vlanCurCfgVlanId,'vlanCurCfgVlanName':vlanCurCfgVlanName,'vlanCurCfgPorts':vlanCurCfgPorts,'vlanCurCfgState':vlanCurCfgState,'vlanCurCfgJumbo':vlanCurCfgJumbo,'vlanCurCfgBwmContract':vlanCurCfgBwmContract,'vlanCurCfgStg':vlanCurCfgStg,'vlanNewCfgTable':vlanNewCfgTable,'vlanNewCfgTableEntry':vlanNewCfgTableEntry,_h:vlanNewCfgVlanId,'vlanNewCfgVlanName':vlanNewCfgVlanName,'vlanNewCfgPorts':vlanNewCfgPorts,'vlanNewCfgState':vlanNewCfgState,'vlanNewCfgJumbo':vlanNewCfgJumbo,'vlanNewCfgAddPort':vlanNewCfgAddPort,'vlanNewCfgRemovePort':vlanNewCfgRemovePort,'vlanNewCfgDelete':vlanNewCfgDelete,'vlanNewCfgBwmContract':vlanNewCfgBwmContract,'vlanNewCfgStg':vlanNewCfgStg,'portmirroring':portmirroring,'pmCurCfgMonitoringPort':pmCurCfgMonitoringPort,'pmNewCfgMonitoringPort':pmNewCfgMonitoringPort,'pmCurCfgMirroredPort':pmCurCfgMirroredPort,'pmNewCfgMirroredPort':pmNewCfgMirroredPort,'pmCurCfgMonitoredTraffic':pmCurCfgMonitoredTraffic,'pmNewCfgMonitoredTraffic':pmNewCfgMonitoredTraffic,'pmCurCfgState':pmCurCfgState,'pmNewCfgState':pmNewCfgState,'pmCurCfgTimeout':pmCurCfgTimeout,'pmNewCfgTimeout':pmNewCfgTimeout,'trunkgroup':trunkgroup,'trunkGroupTableMaxSize':trunkGroupTableMaxSize,'trunkGroupCurCfgTable':trunkGroupCurCfgTable,'trunkGroupCurCfgTableEntry':trunkGroupCurCfgTableEntry,_k:trunkGroupCurCfgIndex,'trunkGroupCurCfgPorts':trunkGroupCurCfgPorts,'trunkGroupCurCfgState':trunkGroupCurCfgState,'trunkGroupCurCfgBwmContract':trunkGroupCurCfgBwmContract,'trunkGroupNewCfgTable':trunkGroupNewCfgTable,'trunkGroupNewCfgTableEntry':trunkGroupNewCfgTableEntry,_n:trunkGroupNewCfgIndex,'trunkGroupNewCfgPorts':trunkGroupNewCfgPorts,'trunkGroupNewCfgAddPort':trunkGroupNewCfgAddPort,'trunkGroupNewCfgRemovePort':trunkGroupNewCfgRemovePort,'trunkGroupNewCfgState':trunkGroupNewCfgState,'trunkGroupNewCfgDelete':trunkGroupNewCfgDelete,'trunkGroupNewCfgBwmContract':trunkGroupNewCfgBwmContract,'portCpuStats':portCpuStats,'portCpuStatsUtilTable':portCpuStatsUtilTable,'portCpuStatsUtilTableEntry':portCpuStatsUtilTableEntry,_o:portCpuStatsUtilIndx,'portCpuAStatsUtil1Second':portCpuAStatsUtil1Second,'portCpuBStatsUtil1Second':portCpuBStatsUtil1Second,'portCpuAStatsUtil4Seconds':portCpuAStatsUtil4Seconds,'portCpuBStatsUtil4Seconds':portCpuBStatsUtil4Seconds,'portCpuAStatsUtil64Seconds':portCpuAStatsUtil64Seconds,'portCpuBStatsUtil64Seconds':portCpuBStatsUtil64Seconds,'port-stats':port_stats,'portStatsTable':portStatsTable,'portStatsTableEntry':portStatsTableEntry,_p:portStatsIndx,'portStatsPhyIfInOctets':portStatsPhyIfInOctets,'portStatsPhyIfInUcastPkts':portStatsPhyIfInUcastPkts,'portStatsPhyIfInNUcastPkts':portStatsPhyIfInNUcastPkts,'portStatsPhyIfInDiscards':portStatsPhyIfInDiscards,'portStatsPhyIfInErrors':portStatsPhyIfInErrors,'portStatsPhyIfInUnknownProtos':portStatsPhyIfInUnknownProtos,'portStatsPhyIfOutOctets':portStatsPhyIfOutOctets,'portStatsPhyIfOutUcastPkts':portStatsPhyIfOutUcastPkts,'portStatsPhyIfOutNUcastPkts':portStatsPhyIfOutNUcastPkts,'portStatsPhyIfOutDiscards':portStatsPhyIfOutDiscards,'portStatsPhyIfOutErrors':portStatsPhyIfOutErrors,'portStatsPhyIfOutQLen':portStatsPhyIfOutQLen,'portStatsPhyIfInBroadcastPkts':portStatsPhyIfInBroadcastPkts,'portStatsPhyIfOutBroadcastPkts':portStatsPhyIfOutBroadcastPkts,'port-info':port_info,'portInfoTable':portInfoTable,'portInfoTableEntry':portInfoTableEntry,_q:portInfoIndx,'portInfoSpeed':portInfoSpeed,'portInfoMode':portInfoMode,'portInfoFlowCtrl':portInfoFlowCtrl,'portInfoLink':portInfoLink,'portInfoPhyIfDescr':portInfoPhyIfDescr,'portInfoPhyIfType':portInfoPhyIfType,'portInfoPhyIfMtu':portInfoPhyIfMtu,'portInfoPhyIfPhysAddress':portInfoPhyIfPhysAddress,'portInfoPhyIfOperStatus':portInfoPhyIfOperStatus,'portInfoPhyIfLastChange':portInfoPhyIfLastChange,'mirrOper':mirrOper,'mirrOperMonitoringPort':mirrOperMonitoringPort,'mirrOperMirroredPort':mirrOperMirroredPort,'mirrOperType':mirrOperType,'mirrOperTimeout':mirrOperTimeout,'mirrOperState':mirrOperState,'mirroring':mirroring,'mirrPortMirr':mirrPortMirr,'pmCurCfgPortMirrState':pmCurCfgPortMirrState,'pmNewCfgPortMirrState':pmNewCfgPortMirrState,'pmCurCfgPortMonitorTable':pmCurCfgPortMonitorTable,'pmCurCfgPortMonitorEntry':pmCurCfgPortMonitorEntry,_r:pmCurCfgPmirrMoniPortIndex,_s:pmCurCfgPmirrMirrPortIndex,'pmCurCfgPmirrDirection':pmCurCfgPmirrDirection,'pmNewCfgPortMonitorTable':pmNewCfgPortMonitorTable,'pmNewCfgPortMonitorEntry':pmNewCfgPortMonitorEntry,_t:pmNewCfgPmirrMoniPortIndex,_u:pmNewCfgPmirrMirrPortIndex,'pmNewCfgPmirrDirection':pmNewCfgPmirrDirection,'pmNewCfgPmirrDelete':pmNewCfgPmirrDelete,'mirrVlanMirr':mirrVlanMirr,'pmCurCfgVlanMirrState':pmCurCfgVlanMirrState,'pmNewCfgVlanMirrState':pmNewCfgVlanMirrState,'pmCurCfgVlanMonitorTable':pmCurCfgVlanMonitorTable,'pmCurCfgVlanMonitorEntry':pmCurCfgVlanMonitorEntry,_v:pmCurCfgVmirrMoniPortIndex,_w:pmCurCfgVmirrMirrVlanIndex,'pmCurCfgVmirrDirection':pmCurCfgVmirrDirection,'pmNewCfgVlanMonitorTable':pmNewCfgVlanMonitorTable,'pmNewCfgVlanMonitorEntry':pmNewCfgVlanMonitorEntry,_x:pmNewCfgVmirrMoniPortIndex,_y:pmNewCfgVmirrMirrVlanIndex,'pmNewCfgVmirrDirection':pmNewCfgVmirrDirection,'pmNewCfgVmirrDelete':pmNewCfgVmirrDelete,'spannTreeGrpCfg':spannTreeGrpCfg,'stgCurCfgTable':stgCurCfgTable,'stgCurCfgTableEntry':stgCurCfgTableEntry,_z:stgCurCfgIndex,'stgCurCfgState':stgCurCfgState,'stgCurCfgVlanBmap1':stgCurCfgVlanBmap1,'stgCurCfgVlanBmap2':stgCurCfgVlanBmap2,'stgNewCfgTable':stgNewCfgTable,'stgNewCfgTableEntry':stgNewCfgTableEntry,_A0:stgNewCfgIndex,'stgNewCfgState':stgNewCfgState,'stgNewCfgDefaultCfg':stgNewCfgDefaultCfg,'stgNewCfgAddVlan':stgNewCfgAddVlan,'stgNewCfgRemoveVlan':stgNewCfgRemoveVlan,'stgNewCfgVlanBmap1':stgNewCfgVlanBmap1,'stgNewCfgVlanBmap2':stgNewCfgVlanBmap2,'stgCurCfgPortTable':stgCurCfgPortTable,'stgCurCfgPortTableEntry':stgCurCfgPortTableEntry,_A1:stgCurCfgStgIndex,_A2:stgCurCfgPortIndex,'stgCurCfgPortState':stgCurCfgPortState,'stgNewCfgPortTable':stgNewCfgPortTable,'stgNewCfgPortTableEntry':stgNewCfgPortTableEntry,_A3:stgNewCfgStgIndex,_A4:stgNewCfgPortIndex,'stgNewCfgPortState':stgNewCfgPortState})