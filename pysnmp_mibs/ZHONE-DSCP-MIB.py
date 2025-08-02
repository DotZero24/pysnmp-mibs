_AH='dscp63map8021p'
_AG='dscp62map8021p'
_AF='dscp61map8021p'
_AE='dscp60map8021p'
_AD='dscp59map8021p'
_AC='dscp58map8021p'
_AB='dscp57map8021p'
_AA='dscp56map8021p'
_A9='dscp55map8021p'
_A8='dscp54map8021p'
_A7='dscp53map8021p'
_A6='dscp52map8021p'
_A5='dscp51map8021p'
_A4='dscp50map8021p'
_A3='dscp49map8021p'
_A2='dscp48map8021p'
_A1='dscp47map8021p'
_A0='dscp46map8021p'
_z='dscp45map8021p'
_y='dscp44map8021p'
_x='dscp43map8021p'
_w='dscp42map8021p'
_v='dscp41map8021p'
_u='dscp40map8021p'
_t='dscp39map8021p'
_s='dscp38map8021p'
_r='dscp37map8021p'
_q='dscp36map8021p'
_p='dscp35map8021p'
_o='dscp34map8021p'
_n='dscp33map8021p'
_m='dscp32map8021p'
_l='dscp31map8021p'
_k='dscp30map8021p'
_j='dscp29map8021p'
_i='dscp28map8021p'
_h='dscp27map8021p'
_g='dscp26map8021p'
_f='dscp25map8021p'
_e='dscp24map8021p'
_d='dscp23map8021p'
_c='dscp22map8021p'
_b='dscp21map8021p'
_a='dscp20map8021p'
_Z='dscp19map8021p'
_Y='dscp18map8021p'
_X='dscp17map8021p'
_W='dscp16map8021p'
_V='dscp15map8021p'
_U='dscp14map8021p'
_T='dscp13map8021p'
_S='dscp12map8021p'
_R='dscp11map8021p'
_Q='dscp10map8021p'
_P='dscp09map8021p'
_O='dscp08map8021p'
_N='dscp07map8021p'
_M='dscp06map8021p'
_L='dscp05map8021p'
_K='dscp04map8021p'
_J='dscp03map8021p'
_I='dscp02map8021p'
_H='dscp01map8021p'
_G='dscp00map8021p'
_F='dscpProfileRowStatus'
_E='dscpIndex'
_D='read-write'
_C='Integer32'
_B='ZHONE-DSCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zhoneIp,=mibBuilder.importSymbols('Zhone','zhoneIp')
dscpProfile=ModuleIdentity((1,3,6,1,4,1,5504,4,1,22))
_DscpProfileTable_Object=MibTable
dscpProfileTable=_DscpProfileTable_Object((1,3,6,1,4,1,5504,4,1,22,1))
if mibBuilder.loadTexts:dscpProfileTable.setStatus(_A)
_DscpProfileEntry_Object=MibTableRow
dscpProfileEntry=_DscpProfileEntry_Object((1,3,6,1,4,1,5504,4,1,22,1,1))
dscpProfileEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dscpProfileEntry.setStatus(_A)
class _DscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DscpIndex_Type.__name__=_C
_DscpIndex_Object=MibTableColumn
dscpIndex=_DscpIndex_Object((1,3,6,1,4,1,5504,4,1,22,1,1,1),_DscpIndex_Type())
dscpIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dscpIndex.setStatus(_A)
_DscpProfileRowStatus_Type=RowStatus
_DscpProfileRowStatus_Object=MibTableColumn
dscpProfileRowStatus=_DscpProfileRowStatus_Object((1,3,6,1,4,1,5504,4,1,22,1,1,2),_DscpProfileRowStatus_Type())
dscpProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dscpProfileRowStatus.setStatus(_A)
class _Dscp00map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp00map8021p_Type.__name__=_C
_Dscp00map8021p_Object=MibTableColumn
dscp00map8021p=_Dscp00map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,3),_Dscp00map8021p_Type())
dscp00map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp00map8021p.setStatus(_A)
class _Dscp01map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp01map8021p_Type.__name__=_C
_Dscp01map8021p_Object=MibTableColumn
dscp01map8021p=_Dscp01map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,4),_Dscp01map8021p_Type())
dscp01map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp01map8021p.setStatus(_A)
class _Dscp02map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp02map8021p_Type.__name__=_C
_Dscp02map8021p_Object=MibTableColumn
dscp02map8021p=_Dscp02map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,5),_Dscp02map8021p_Type())
dscp02map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp02map8021p.setStatus(_A)
class _Dscp03map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp03map8021p_Type.__name__=_C
_Dscp03map8021p_Object=MibTableColumn
dscp03map8021p=_Dscp03map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,6),_Dscp03map8021p_Type())
dscp03map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp03map8021p.setStatus(_A)
class _Dscp04map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp04map8021p_Type.__name__=_C
_Dscp04map8021p_Object=MibTableColumn
dscp04map8021p=_Dscp04map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,7),_Dscp04map8021p_Type())
dscp04map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp04map8021p.setStatus(_A)
class _Dscp05map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp05map8021p_Type.__name__=_C
_Dscp05map8021p_Object=MibTableColumn
dscp05map8021p=_Dscp05map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,8),_Dscp05map8021p_Type())
dscp05map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp05map8021p.setStatus(_A)
class _Dscp06map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp06map8021p_Type.__name__=_C
_Dscp06map8021p_Object=MibTableColumn
dscp06map8021p=_Dscp06map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,9),_Dscp06map8021p_Type())
dscp06map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp06map8021p.setStatus(_A)
class _Dscp07map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp07map8021p_Type.__name__=_C
_Dscp07map8021p_Object=MibTableColumn
dscp07map8021p=_Dscp07map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,10),_Dscp07map8021p_Type())
dscp07map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp07map8021p.setStatus(_A)
class _Dscp08map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp08map8021p_Type.__name__=_C
_Dscp08map8021p_Object=MibTableColumn
dscp08map8021p=_Dscp08map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,11),_Dscp08map8021p_Type())
dscp08map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp08map8021p.setStatus(_A)
class _Dscp09map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp09map8021p_Type.__name__=_C
_Dscp09map8021p_Object=MibTableColumn
dscp09map8021p=_Dscp09map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,12),_Dscp09map8021p_Type())
dscp09map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp09map8021p.setStatus(_A)
class _Dscp10map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp10map8021p_Type.__name__=_C
_Dscp10map8021p_Object=MibTableColumn
dscp10map8021p=_Dscp10map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,13),_Dscp10map8021p_Type())
dscp10map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp10map8021p.setStatus(_A)
class _Dscp11map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp11map8021p_Type.__name__=_C
_Dscp11map8021p_Object=MibTableColumn
dscp11map8021p=_Dscp11map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,14),_Dscp11map8021p_Type())
dscp11map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp11map8021p.setStatus(_A)
class _Dscp12map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp12map8021p_Type.__name__=_C
_Dscp12map8021p_Object=MibTableColumn
dscp12map8021p=_Dscp12map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,15),_Dscp12map8021p_Type())
dscp12map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp12map8021p.setStatus(_A)
class _Dscp13map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp13map8021p_Type.__name__=_C
_Dscp13map8021p_Object=MibTableColumn
dscp13map8021p=_Dscp13map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,16),_Dscp13map8021p_Type())
dscp13map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp13map8021p.setStatus(_A)
class _Dscp14map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp14map8021p_Type.__name__=_C
_Dscp14map8021p_Object=MibTableColumn
dscp14map8021p=_Dscp14map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,17),_Dscp14map8021p_Type())
dscp14map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp14map8021p.setStatus(_A)
class _Dscp15map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp15map8021p_Type.__name__=_C
_Dscp15map8021p_Object=MibTableColumn
dscp15map8021p=_Dscp15map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,18),_Dscp15map8021p_Type())
dscp15map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp15map8021p.setStatus(_A)
class _Dscp16map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp16map8021p_Type.__name__=_C
_Dscp16map8021p_Object=MibTableColumn
dscp16map8021p=_Dscp16map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,19),_Dscp16map8021p_Type())
dscp16map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp16map8021p.setStatus(_A)
class _Dscp17map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp17map8021p_Type.__name__=_C
_Dscp17map8021p_Object=MibTableColumn
dscp17map8021p=_Dscp17map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,20),_Dscp17map8021p_Type())
dscp17map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp17map8021p.setStatus(_A)
class _Dscp18map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp18map8021p_Type.__name__=_C
_Dscp18map8021p_Object=MibTableColumn
dscp18map8021p=_Dscp18map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,21),_Dscp18map8021p_Type())
dscp18map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp18map8021p.setStatus(_A)
class _Dscp19map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp19map8021p_Type.__name__=_C
_Dscp19map8021p_Object=MibTableColumn
dscp19map8021p=_Dscp19map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,22),_Dscp19map8021p_Type())
dscp19map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp19map8021p.setStatus(_A)
class _Dscp20map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp20map8021p_Type.__name__=_C
_Dscp20map8021p_Object=MibTableColumn
dscp20map8021p=_Dscp20map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,23),_Dscp20map8021p_Type())
dscp20map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp20map8021p.setStatus(_A)
class _Dscp21map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp21map8021p_Type.__name__=_C
_Dscp21map8021p_Object=MibTableColumn
dscp21map8021p=_Dscp21map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,24),_Dscp21map8021p_Type())
dscp21map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp21map8021p.setStatus(_A)
class _Dscp22map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp22map8021p_Type.__name__=_C
_Dscp22map8021p_Object=MibTableColumn
dscp22map8021p=_Dscp22map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,25),_Dscp22map8021p_Type())
dscp22map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp22map8021p.setStatus(_A)
class _Dscp23map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp23map8021p_Type.__name__=_C
_Dscp23map8021p_Object=MibTableColumn
dscp23map8021p=_Dscp23map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,26),_Dscp23map8021p_Type())
dscp23map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp23map8021p.setStatus(_A)
class _Dscp24map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp24map8021p_Type.__name__=_C
_Dscp24map8021p_Object=MibTableColumn
dscp24map8021p=_Dscp24map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,27),_Dscp24map8021p_Type())
dscp24map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp24map8021p.setStatus(_A)
class _Dscp25map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp25map8021p_Type.__name__=_C
_Dscp25map8021p_Object=MibTableColumn
dscp25map8021p=_Dscp25map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,28),_Dscp25map8021p_Type())
dscp25map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp25map8021p.setStatus(_A)
class _Dscp26map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp26map8021p_Type.__name__=_C
_Dscp26map8021p_Object=MibTableColumn
dscp26map8021p=_Dscp26map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,29),_Dscp26map8021p_Type())
dscp26map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp26map8021p.setStatus(_A)
class _Dscp27map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp27map8021p_Type.__name__=_C
_Dscp27map8021p_Object=MibTableColumn
dscp27map8021p=_Dscp27map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,30),_Dscp27map8021p_Type())
dscp27map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp27map8021p.setStatus(_A)
class _Dscp28map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp28map8021p_Type.__name__=_C
_Dscp28map8021p_Object=MibTableColumn
dscp28map8021p=_Dscp28map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,31),_Dscp28map8021p_Type())
dscp28map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp28map8021p.setStatus(_A)
class _Dscp29map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp29map8021p_Type.__name__=_C
_Dscp29map8021p_Object=MibTableColumn
dscp29map8021p=_Dscp29map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,32),_Dscp29map8021p_Type())
dscp29map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp29map8021p.setStatus(_A)
class _Dscp30map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp30map8021p_Type.__name__=_C
_Dscp30map8021p_Object=MibTableColumn
dscp30map8021p=_Dscp30map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,33),_Dscp30map8021p_Type())
dscp30map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp30map8021p.setStatus(_A)
class _Dscp31map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp31map8021p_Type.__name__=_C
_Dscp31map8021p_Object=MibTableColumn
dscp31map8021p=_Dscp31map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,34),_Dscp31map8021p_Type())
dscp31map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp31map8021p.setStatus(_A)
class _Dscp32map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp32map8021p_Type.__name__=_C
_Dscp32map8021p_Object=MibTableColumn
dscp32map8021p=_Dscp32map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,35),_Dscp32map8021p_Type())
dscp32map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp32map8021p.setStatus(_A)
class _Dscp33map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp33map8021p_Type.__name__=_C
_Dscp33map8021p_Object=MibTableColumn
dscp33map8021p=_Dscp33map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,36),_Dscp33map8021p_Type())
dscp33map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp33map8021p.setStatus(_A)
class _Dscp34map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp34map8021p_Type.__name__=_C
_Dscp34map8021p_Object=MibTableColumn
dscp34map8021p=_Dscp34map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,37),_Dscp34map8021p_Type())
dscp34map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp34map8021p.setStatus(_A)
class _Dscp35map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp35map8021p_Type.__name__=_C
_Dscp35map8021p_Object=MibTableColumn
dscp35map8021p=_Dscp35map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,38),_Dscp35map8021p_Type())
dscp35map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp35map8021p.setStatus(_A)
class _Dscp36map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp36map8021p_Type.__name__=_C
_Dscp36map8021p_Object=MibTableColumn
dscp36map8021p=_Dscp36map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,39),_Dscp36map8021p_Type())
dscp36map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp36map8021p.setStatus(_A)
class _Dscp37map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp37map8021p_Type.__name__=_C
_Dscp37map8021p_Object=MibTableColumn
dscp37map8021p=_Dscp37map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,40),_Dscp37map8021p_Type())
dscp37map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp37map8021p.setStatus(_A)
class _Dscp38map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp38map8021p_Type.__name__=_C
_Dscp38map8021p_Object=MibTableColumn
dscp38map8021p=_Dscp38map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,41),_Dscp38map8021p_Type())
dscp38map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp38map8021p.setStatus(_A)
class _Dscp39map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp39map8021p_Type.__name__=_C
_Dscp39map8021p_Object=MibTableColumn
dscp39map8021p=_Dscp39map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,42),_Dscp39map8021p_Type())
dscp39map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp39map8021p.setStatus(_A)
class _Dscp40map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp40map8021p_Type.__name__=_C
_Dscp40map8021p_Object=MibTableColumn
dscp40map8021p=_Dscp40map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,43),_Dscp40map8021p_Type())
dscp40map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp40map8021p.setStatus(_A)
class _Dscp41map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp41map8021p_Type.__name__=_C
_Dscp41map8021p_Object=MibTableColumn
dscp41map8021p=_Dscp41map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,44),_Dscp41map8021p_Type())
dscp41map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp41map8021p.setStatus(_A)
class _Dscp42map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp42map8021p_Type.__name__=_C
_Dscp42map8021p_Object=MibTableColumn
dscp42map8021p=_Dscp42map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,45),_Dscp42map8021p_Type())
dscp42map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp42map8021p.setStatus(_A)
class _Dscp43map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp43map8021p_Type.__name__=_C
_Dscp43map8021p_Object=MibTableColumn
dscp43map8021p=_Dscp43map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,46),_Dscp43map8021p_Type())
dscp43map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp43map8021p.setStatus(_A)
class _Dscp44map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp44map8021p_Type.__name__=_C
_Dscp44map8021p_Object=MibTableColumn
dscp44map8021p=_Dscp44map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,47),_Dscp44map8021p_Type())
dscp44map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp44map8021p.setStatus(_A)
class _Dscp45map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp45map8021p_Type.__name__=_C
_Dscp45map8021p_Object=MibTableColumn
dscp45map8021p=_Dscp45map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,48),_Dscp45map8021p_Type())
dscp45map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp45map8021p.setStatus(_A)
class _Dscp46map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp46map8021p_Type.__name__=_C
_Dscp46map8021p_Object=MibTableColumn
dscp46map8021p=_Dscp46map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,49),_Dscp46map8021p_Type())
dscp46map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp46map8021p.setStatus(_A)
class _Dscp47map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp47map8021p_Type.__name__=_C
_Dscp47map8021p_Object=MibTableColumn
dscp47map8021p=_Dscp47map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,50),_Dscp47map8021p_Type())
dscp47map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp47map8021p.setStatus(_A)
class _Dscp48map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp48map8021p_Type.__name__=_C
_Dscp48map8021p_Object=MibTableColumn
dscp48map8021p=_Dscp48map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,51),_Dscp48map8021p_Type())
dscp48map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp48map8021p.setStatus(_A)
class _Dscp49map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp49map8021p_Type.__name__=_C
_Dscp49map8021p_Object=MibTableColumn
dscp49map8021p=_Dscp49map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,52),_Dscp49map8021p_Type())
dscp49map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp49map8021p.setStatus(_A)
class _Dscp50map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp50map8021p_Type.__name__=_C
_Dscp50map8021p_Object=MibTableColumn
dscp50map8021p=_Dscp50map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,53),_Dscp50map8021p_Type())
dscp50map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp50map8021p.setStatus(_A)
class _Dscp51map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp51map8021p_Type.__name__=_C
_Dscp51map8021p_Object=MibTableColumn
dscp51map8021p=_Dscp51map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,54),_Dscp51map8021p_Type())
dscp51map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp51map8021p.setStatus(_A)
class _Dscp52map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp52map8021p_Type.__name__=_C
_Dscp52map8021p_Object=MibTableColumn
dscp52map8021p=_Dscp52map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,55),_Dscp52map8021p_Type())
dscp52map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp52map8021p.setStatus(_A)
class _Dscp53map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp53map8021p_Type.__name__=_C
_Dscp53map8021p_Object=MibTableColumn
dscp53map8021p=_Dscp53map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,56),_Dscp53map8021p_Type())
dscp53map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp53map8021p.setStatus(_A)
class _Dscp54map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp54map8021p_Type.__name__=_C
_Dscp54map8021p_Object=MibTableColumn
dscp54map8021p=_Dscp54map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,57),_Dscp54map8021p_Type())
dscp54map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp54map8021p.setStatus(_A)
class _Dscp55map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp55map8021p_Type.__name__=_C
_Dscp55map8021p_Object=MibTableColumn
dscp55map8021p=_Dscp55map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,58),_Dscp55map8021p_Type())
dscp55map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp55map8021p.setStatus(_A)
class _Dscp56map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp56map8021p_Type.__name__=_C
_Dscp56map8021p_Object=MibTableColumn
dscp56map8021p=_Dscp56map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,59),_Dscp56map8021p_Type())
dscp56map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp56map8021p.setStatus(_A)
class _Dscp57map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp57map8021p_Type.__name__=_C
_Dscp57map8021p_Object=MibTableColumn
dscp57map8021p=_Dscp57map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,60),_Dscp57map8021p_Type())
dscp57map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp57map8021p.setStatus(_A)
class _Dscp58map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp58map8021p_Type.__name__=_C
_Dscp58map8021p_Object=MibTableColumn
dscp58map8021p=_Dscp58map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,61),_Dscp58map8021p_Type())
dscp58map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp58map8021p.setStatus(_A)
class _Dscp59map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp59map8021p_Type.__name__=_C
_Dscp59map8021p_Object=MibTableColumn
dscp59map8021p=_Dscp59map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,62),_Dscp59map8021p_Type())
dscp59map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp59map8021p.setStatus(_A)
class _Dscp60map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp60map8021p_Type.__name__=_C
_Dscp60map8021p_Object=MibTableColumn
dscp60map8021p=_Dscp60map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,63),_Dscp60map8021p_Type())
dscp60map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp60map8021p.setStatus(_A)
class _Dscp61map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp61map8021p_Type.__name__=_C
_Dscp61map8021p_Object=MibTableColumn
dscp61map8021p=_Dscp61map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,64),_Dscp61map8021p_Type())
dscp61map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp61map8021p.setStatus(_A)
class _Dscp62map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp62map8021p_Type.__name__=_C
_Dscp62map8021p_Object=MibTableColumn
dscp62map8021p=_Dscp62map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,65),_Dscp62map8021p_Type())
dscp62map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp62map8021p.setStatus(_A)
class _Dscp63map8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dscp63map8021p_Type.__name__=_C
_Dscp63map8021p_Object=MibTableColumn
dscp63map8021p=_Dscp63map8021p_Object((1,3,6,1,4,1,5504,4,1,22,1,1,66),_Dscp63map8021p_Type())
dscp63map8021p.setMaxAccess(_D)
if mibBuilder.loadTexts:dscp63map8021p.setStatus(_A)
dscpProfileGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,22,2))
dscpProfileGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:dscpProfileGroup.setStatus(_A)
dscpProfileGroupObjectGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,22,3))
dscpProfileGroupObjectGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:dscpProfileGroupObjectGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dscpProfile':dscpProfile,'dscpProfileTable':dscpProfileTable,'dscpProfileEntry':dscpProfileEntry,_E:dscpIndex,_F:dscpProfileRowStatus,_G:dscp00map8021p,_H:dscp01map8021p,_I:dscp02map8021p,_J:dscp03map8021p,_K:dscp04map8021p,_L:dscp05map8021p,_M:dscp06map8021p,_N:dscp07map8021p,_O:dscp08map8021p,_P:dscp09map8021p,_Q:dscp10map8021p,_R:dscp11map8021p,_S:dscp12map8021p,_T:dscp13map8021p,_U:dscp14map8021p,_V:dscp15map8021p,_W:dscp16map8021p,_X:dscp17map8021p,_Y:dscp18map8021p,_Z:dscp19map8021p,_a:dscp20map8021p,_b:dscp21map8021p,_c:dscp22map8021p,_d:dscp23map8021p,_e:dscp24map8021p,_f:dscp25map8021p,_g:dscp26map8021p,_h:dscp27map8021p,_i:dscp28map8021p,_j:dscp29map8021p,_k:dscp30map8021p,_l:dscp31map8021p,_m:dscp32map8021p,_n:dscp33map8021p,_o:dscp34map8021p,_p:dscp35map8021p,_q:dscp36map8021p,_r:dscp37map8021p,_s:dscp38map8021p,_t:dscp39map8021p,_u:dscp40map8021p,_v:dscp41map8021p,_w:dscp42map8021p,_x:dscp43map8021p,_y:dscp44map8021p,_z:dscp45map8021p,_A0:dscp46map8021p,_A1:dscp47map8021p,_A2:dscp48map8021p,_A3:dscp49map8021p,_A4:dscp50map8021p,_A5:dscp51map8021p,_A6:dscp52map8021p,_A7:dscp53map8021p,_A8:dscp54map8021p,_A9:dscp55map8021p,_AA:dscp56map8021p,_AB:dscp57map8021p,_AC:dscp58map8021p,_AD:dscp59map8021p,_AE:dscp60map8021p,_AF:dscp61map8021p,_AG:dscp62map8021p,_AH:dscp63map8021p,'dscpProfileGroup':dscpProfileGroup,'dscpProfileGroupObjectGroup':dscpProfileGroupObjectGroup})