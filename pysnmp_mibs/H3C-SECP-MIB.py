_H='read-only'
_G='not-accessible'
_F='h3cSecpRuleID'
_E='h3cSecpIPVersion'
_D='Unsigned32'
_C='Integer32'
_B='H3C-SECP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cSecp=ModuleIdentity((1,3,6,1,4,1,2011,10,2,166))
if mibBuilder.loadTexts:h3cSecp.setRevisions(('2016-12-19 16:05',))
_H3cSecpObjects_ObjectIdentity=ObjectIdentity
h3cSecpObjects=_H3cSecpObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,166,1))
_H3cSecpRunningInfoTable_Object=MibTable
h3cSecpRunningInfoTable=_H3cSecpRunningInfoTable_Object((1,3,6,1,4,1,2011,10,2,166,1,1))
if mibBuilder.loadTexts:h3cSecpRunningInfoTable.setStatus(_A)
_H3cSecpRunningInfoEntry_Object=MibTableRow
h3cSecpRunningInfoEntry=_H3cSecpRunningInfoEntry_Object((1,3,6,1,4,1,2011,10,2,166,1,1,1))
h3cSecpRunningInfoEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:h3cSecpRunningInfoEntry.setStatus(_A)
class _H3cSecpIPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_H3cSecpIPVersion_Type.__name__=_C
_H3cSecpIPVersion_Object=MibTableColumn
h3cSecpIPVersion=_H3cSecpIPVersion_Object((1,3,6,1,4,1,2011,10,2,166,1,1,1,1),_H3cSecpIPVersion_Type())
h3cSecpIPVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSecpIPVersion.setStatus(_A)
class _H3cSecpRuleID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_H3cSecpRuleID_Type.__name__=_D
_H3cSecpRuleID_Object=MibTableColumn
h3cSecpRuleID=_H3cSecpRuleID_Object((1,3,6,1,4,1,2011,10,2,166,1,1,1,2),_H3cSecpRuleID_Type())
h3cSecpRuleID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSecpRuleID.setStatus(_A)
_H3cSecpMatchPacketCount_Type=Counter64
_H3cSecpMatchPacketCount_Object=MibTableColumn
h3cSecpMatchPacketCount=_H3cSecpMatchPacketCount_Object((1,3,6,1,4,1,2011,10,2,166,1,1,1,3),_H3cSecpMatchPacketCount_Type())
h3cSecpMatchPacketCount.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecpMatchPacketCount.setStatus(_A)
_H3cSecpLastMatchTime_Type=Unsigned32
_H3cSecpLastMatchTime_Object=MibTableColumn
h3cSecpLastMatchTime=_H3cSecpLastMatchTime_Object((1,3,6,1,4,1,2011,10,2,166,1,1,1,4),_H3cSecpLastMatchTime_Type())
h3cSecpLastMatchTime.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecpLastMatchTime.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSecp':h3cSecp,'h3cSecpObjects':h3cSecpObjects,'h3cSecpRunningInfoTable':h3cSecpRunningInfoTable,'h3cSecpRunningInfoEntry':h3cSecpRunningInfoEntry,_E:h3cSecpIPVersion,_F:h3cSecpRuleID,'h3cSecpMatchPacketCount':h3cSecpMatchPacketCount,'h3cSecpLastMatchTime':h3cSecpLastMatchTime})