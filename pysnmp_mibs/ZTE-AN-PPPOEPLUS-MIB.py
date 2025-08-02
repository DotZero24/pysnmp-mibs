_G='zxAnPortLocatingPppoePlusifIndex'
_F='ZTE-AN-PPPOEPLUS-MIB'
_E='disable'
_D='enable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxAnPortLocatingMib,=mibBuilder.importSymbols('ZTE-AN-PORT-LOCATING-MIB','zxAnPortLocatingMib')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnPppoePlusMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,32,40))
class _ZxAnPppoeIAEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnPppoeIAEnable_Type.__name__=_B
_ZxAnPppoeIAEnable_Object=MibScalar
zxAnPppoeIAEnable=_ZxAnPppoeIAEnable_Object((1,3,6,1,4,1,3902,1015,32,40,1),_ZxAnPppoeIAEnable_Type())
zxAnPppoeIAEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPppoeIAEnable.setStatus(_A)
_ZxAnPortLocatingPppoePlusTable_Object=MibTable
zxAnPortLocatingPppoePlusTable=_ZxAnPortLocatingPppoePlusTable_Object((1,3,6,1,4,1,3902,1015,32,40,10))
if mibBuilder.loadTexts:zxAnPortLocatingPppoePlusTable.setStatus(_A)
_ZxAnPortLocatingPppoePlusEntry_Object=MibTableRow
zxAnPortLocatingPppoePlusEntry=_ZxAnPortLocatingPppoePlusEntry_Object((1,3,6,1,4,1,3902,1015,32,40,10,1))
zxAnPortLocatingPppoePlusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnPortLocatingPppoePlusEntry.setStatus(_A)
_ZxAnPortLocatingPppoePlusifIndex_Type=ZxAnIfindex
_ZxAnPortLocatingPppoePlusifIndex_Object=MibTableColumn
zxAnPortLocatingPppoePlusifIndex=_ZxAnPortLocatingPppoePlusifIndex_Object((1,3,6,1,4,1,3902,1015,32,40,10,1,1),_ZxAnPortLocatingPppoePlusifIndex_Type())
zxAnPortLocatingPppoePlusifIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnPortLocatingPppoePlusifIndex.setStatus(_A)
class _ZxAnPppoeIAIfConfEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnPppoeIAIfConfEnable_Type.__name__=_B
_ZxAnPppoeIAIfConfEnable_Object=MibTableColumn
zxAnPppoeIAIfConfEnable=_ZxAnPppoeIAIfConfEnable_Object((1,3,6,1,4,1,3902,1015,32,40,10,1,2),_ZxAnPppoeIAIfConfEnable_Type())
zxAnPppoeIAIfConfEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPppoeIAIfConfEnable.setStatus(_A)
class _ZxAnPppoeIAIfConfTrust_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ZxAnPppoeIAIfConfTrust_Type.__name__=_B
_ZxAnPppoeIAIfConfTrust_Object=MibTableColumn
zxAnPppoeIAIfConfTrust=_ZxAnPppoeIAIfConfTrust_Object((1,3,6,1,4,1,3902,1015,32,40,10,1,3),_ZxAnPppoeIAIfConfTrust_Type())
zxAnPppoeIAIfConfTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPppoeIAIfConfTrust.setStatus(_A)
class _ZxAnPppoeIAIfConfPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('keep',1),('replace',2),('discard',3),('add',4)))
_ZxAnPppoeIAIfConfPolicy_Type.__name__=_B
_ZxAnPppoeIAIfConfPolicy_Object=MibTableColumn
zxAnPppoeIAIfConfPolicy=_ZxAnPppoeIAIfConfPolicy_Object((1,3,6,1,4,1,3902,1015,32,40,10,1,4),_ZxAnPppoeIAIfConfPolicy_Type())
zxAnPppoeIAIfConfPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPppoeIAIfConfPolicy.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zxAnPppoePlusMib':zxAnPppoePlusMib,'zxAnPppoeIAEnable':zxAnPppoeIAEnable,'zxAnPortLocatingPppoePlusTable':zxAnPortLocatingPppoePlusTable,'zxAnPortLocatingPppoePlusEntry':zxAnPortLocatingPppoePlusEntry,_G:zxAnPortLocatingPppoePlusifIndex,'zxAnPppoeIAIfConfEnable':zxAnPppoeIAIfConfEnable,'zxAnPppoeIAIfConfTrust':zxAnPppoeIAIfConfTrust,'zxAnPppoeIAIfConfPolicy':zxAnPppoeIAIfConfPolicy})