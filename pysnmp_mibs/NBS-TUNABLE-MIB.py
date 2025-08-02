_E='nbsTunableChannelIfIndex'
_D='NBS-TUNABLE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsTunableMib=ModuleIdentity((1,3,6,1,4,1,629,203))
_NbsTunableGrp_ObjectIdentity=ObjectIdentity
nbsTunableGrp=_NbsTunableGrp_ObjectIdentity((1,3,6,1,4,1,629,203,1))
if mibBuilder.loadTexts:nbsTunableGrp.setStatus(_A)
_NbsTunableChannelTableSize_Type=Unsigned32
_NbsTunableChannelTableSize_Object=MibScalar
nbsTunableChannelTableSize=_NbsTunableChannelTableSize_Object((1,3,6,1,4,1,629,203,1,1),_NbsTunableChannelTableSize_Type())
nbsTunableChannelTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelTableSize.setStatus(_A)
_NbsTunableChannelTable_Object=MibTable
nbsTunableChannelTable=_NbsTunableChannelTable_Object((1,3,6,1,4,1,629,203,1,2))
if mibBuilder.loadTexts:nbsTunableChannelTable.setStatus(_A)
_NbsTunableChannelEntry_Object=MibTableRow
nbsTunableChannelEntry=_NbsTunableChannelEntry_Object((1,3,6,1,4,1,629,203,1,2,1))
nbsTunableChannelEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nbsTunableChannelEntry.setStatus(_A)
_NbsTunableChannelIfIndex_Type=InterfaceIndex
_NbsTunableChannelIfIndex_Object=MibTableColumn
nbsTunableChannelIfIndex=_NbsTunableChannelIfIndex_Object((1,3,6,1,4,1,629,203,1,2,1,1),_NbsTunableChannelIfIndex_Type())
nbsTunableChannelIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelIfIndex.setStatus(_A)
class _NbsTunableChannelFreqStart_Type(Integer32):defaultValue=190100
_NbsTunableChannelFreqStart_Type.__name__=_C
_NbsTunableChannelFreqStart_Object=MibTableColumn
nbsTunableChannelFreqStart=_NbsTunableChannelFreqStart_Object((1,3,6,1,4,1,629,203,1,2,1,2),_NbsTunableChannelFreqStart_Type())
nbsTunableChannelFreqStart.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelFreqStart.setStatus(_A)
class _NbsTunableChannelFreqEnd_Type(Integer32):defaultValue=197200
_NbsTunableChannelFreqEnd_Type.__name__=_C
_NbsTunableChannelFreqEnd_Object=MibTableColumn
nbsTunableChannelFreqEnd=_NbsTunableChannelFreqEnd_Object((1,3,6,1,4,1,629,203,1,2,1,3),_NbsTunableChannelFreqEnd_Type())
nbsTunableChannelFreqEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelFreqEnd.setStatus(_A)
class _NbsTunableChannelFreqStep_Type(Integer32):defaultValue=100
_NbsTunableChannelFreqStep_Type.__name__=_C
_NbsTunableChannelFreqStep_Object=MibTableColumn
nbsTunableChannelFreqStep=_NbsTunableChannelFreqStep_Object((1,3,6,1,4,1,629,203,1,2,1,4),_NbsTunableChannelFreqStep_Type())
nbsTunableChannelFreqStep.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelFreqStep.setStatus(_A)
class _NbsTunableChannelFreqExponent_Type(Integer32):defaultValue=9
_NbsTunableChannelFreqExponent_Type.__name__=_C
_NbsTunableChannelFreqExponent_Object=MibTableColumn
nbsTunableChannelFreqExponent=_NbsTunableChannelFreqExponent_Object((1,3,6,1,4,1,629,203,1,2,1,5),_NbsTunableChannelFreqExponent_Type())
nbsTunableChannelFreqExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelFreqExponent.setStatus(_A)
_NbsTunableChannelFreqAdmin_Type=Integer32
_NbsTunableChannelFreqAdmin_Object=MibTableColumn
nbsTunableChannelFreqAdmin=_NbsTunableChannelFreqAdmin_Object((1,3,6,1,4,1,629,203,1,2,1,6),_NbsTunableChannelFreqAdmin_Type())
nbsTunableChannelFreqAdmin.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsTunableChannelFreqAdmin.setStatus(_A)
_NbsTunableChannelFreqOper_Type=Integer32
_NbsTunableChannelFreqOper_Object=MibTableColumn
nbsTunableChannelFreqOper=_NbsTunableChannelFreqOper_Object((1,3,6,1,4,1,629,203,1,2,1,7),_NbsTunableChannelFreqOper_Type())
nbsTunableChannelFreqOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelFreqOper.setStatus(_A)
_NbsTunableChannelFreqDefault_Type=Integer32
_NbsTunableChannelFreqDefault_Object=MibTableColumn
nbsTunableChannelFreqDefault=_NbsTunableChannelFreqDefault_Object((1,3,6,1,4,1,629,203,1,2,1,8),_NbsTunableChannelFreqDefault_Type())
nbsTunableChannelFreqDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTunableChannelFreqDefault.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsTunableMib':nbsTunableMib,'nbsTunableGrp':nbsTunableGrp,'nbsTunableChannelTableSize':nbsTunableChannelTableSize,'nbsTunableChannelTable':nbsTunableChannelTable,'nbsTunableChannelEntry':nbsTunableChannelEntry,_E:nbsTunableChannelIfIndex,'nbsTunableChannelFreqStart':nbsTunableChannelFreqStart,'nbsTunableChannelFreqEnd':nbsTunableChannelFreqEnd,'nbsTunableChannelFreqStep':nbsTunableChannelFreqStep,'nbsTunableChannelFreqExponent':nbsTunableChannelFreqExponent,'nbsTunableChannelFreqAdmin':nbsTunableChannelFreqAdmin,'nbsTunableChannelFreqOper':nbsTunableChannelFreqOper,'nbsTunableChannelFreqDefault':nbsTunableChannelFreqDefault})