_G='read-only'
_F='DisplayString'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkPortSecurityMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,12))
if mibBuilder.loadTexts:tplinkPortSecurityMIB.setRevisions(('2012-12-13 00:00',))
_TplinkPortSecurityMIBObjects_ObjectIdentity=ObjectIdentity
tplinkPortSecurityMIBObjects=_TplinkPortSecurityMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,12,1))
_TpPortSecurityTable_Object=MibTable
tpPortSecurityTable=_TpPortSecurityTable_Object((1,3,6,1,4,1,11863,6,12,1,1))
if mibBuilder.loadTexts:tpPortSecurityTable.setStatus(_A)
_TpPortSecurityEntry_Object=MibTableRow
tpPortSecurityEntry=_TpPortSecurityEntry_Object((1,3,6,1,4,1,11863,6,12,1,1,1))
tpPortSecurityEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tpPortSecurityEntry.setStatus(_A)
class _TpPortSecurityPortIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpPortSecurityPortIndex_Type.__name__=_F
_TpPortSecurityPortIndex_Object=MibTableColumn
tpPortSecurityPortIndex=_TpPortSecurityPortIndex_Object((1,3,6,1,4,1,11863,6,12,1,1,1,1),_TpPortSecurityPortIndex_Type())
tpPortSecurityPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:tpPortSecurityPortIndex.setStatus(_A)
class _TpPortSecurityMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_TpPortSecurityMaxNum_Type.__name__=_B
_TpPortSecurityMaxNum_Object=MibTableColumn
tpPortSecurityMaxNum=_TpPortSecurityMaxNum_Object((1,3,6,1,4,1,11863,6,12,1,1,1,2),_TpPortSecurityMaxNum_Type())
tpPortSecurityMaxNum.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPortSecurityMaxNum.setStatus(_A)
_TpPortSecurityLearnNum_Type=Integer32
_TpPortSecurityLearnNum_Object=MibTableColumn
tpPortSecurityLearnNum=_TpPortSecurityLearnNum_Object((1,3,6,1,4,1,11863,6,12,1,1,1,3),_TpPortSecurityLearnNum_Type())
tpPortSecurityLearnNum.setMaxAccess(_G)
if mibBuilder.loadTexts:tpPortSecurityLearnNum.setStatus(_A)
class _TpPortSecurityLearnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dynamic',0),('static',1),('permanent',2)))
_TpPortSecurityLearnMode_Type.__name__=_B
_TpPortSecurityLearnMode_Object=MibTableColumn
tpPortSecurityLearnMode=_TpPortSecurityLearnMode_Object((1,3,6,1,4,1,11863,6,12,1,1,1,4),_TpPortSecurityLearnMode_Type())
tpPortSecurityLearnMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPortSecurityLearnMode.setStatus(_A)
class _TpPortSecurityPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disable',0),('forward',1),('drop',2)))
_TpPortSecurityPortStatus_Type.__name__=_B
_TpPortSecurityPortStatus_Object=MibTableColumn
tpPortSecurityPortStatus=_TpPortSecurityPortStatus_Object((1,3,6,1,4,1,11863,6,12,1,1,1,5),_TpPortSecurityPortStatus_Type())
tpPortSecurityPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPortSecurityPortStatus.setStatus(_A)
_TplinkPortSecurityNotifications_ObjectIdentity=ObjectIdentity
tplinkPortSecurityNotifications=_TplinkPortSecurityNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,12,2))
mibBuilder.exportSymbols('TPLINK-PORTSECURITY-MIB',**{'tplinkPortSecurityMIB':tplinkPortSecurityMIB,'tplinkPortSecurityMIBObjects':tplinkPortSecurityMIBObjects,'tpPortSecurityTable':tpPortSecurityTable,'tpPortSecurityEntry':tpPortSecurityEntry,'tpPortSecurityPortIndex':tpPortSecurityPortIndex,'tpPortSecurityMaxNum':tpPortSecurityMaxNum,'tpPortSecurityLearnNum':tpPortSecurityLearnNum,'tpPortSecurityLearnMode':tpPortSecurityLearnMode,'tpPortSecurityPortStatus':tpPortSecurityPortStatus,'tplinkPortSecurityNotifications':tplinkPortSecurityNotifications})