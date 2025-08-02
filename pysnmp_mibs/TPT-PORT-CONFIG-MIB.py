_F='portConfigPort'
_E='portConfigSlot'
_D='TPT-PORT-CONFIG-MIB'
_C='default'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_port_config_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,4))
if mibBuilder.loadTexts:tpt_port_config_objs.setRevisions(('2016-05-25 18:54',))
class LineSpeed(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_C,0),('gigabit',1),('hundred-megabit',2),('ten-megabit',3),('ten-gigabit',4),('fourty-gigabit',5)))
class DuplexSetting(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_C,0),('half',1),('full',2)))
class AutoNegotiation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_C,0),('on',1),('off',2)))
class EnabledOrNot(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class FailoverAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('block',0),('permit',1)))
class LinkDownMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('hub',0),('breaker',1),('wire',2)))
_PortConfigTable_Object=MibTable
portConfigTable=_PortConfigTable_Object((1,3,6,1,4,1,10734,3,3,2,4,1))
if mibBuilder.loadTexts:portConfigTable.setStatus(_A)
_PortConfigEntry_Object=MibTableRow
portConfigEntry=_PortConfigEntry_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1))
portConfigEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:portConfigEntry.setStatus(_A)
_PortConfigSlot_Type=Unsigned32
_PortConfigSlot_Object=MibTableColumn
portConfigSlot=_PortConfigSlot_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,1),_PortConfigSlot_Type())
portConfigSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigSlot.setStatus(_A)
_PortConfigPort_Type=Unsigned32
_PortConfigPort_Object=MibTableColumn
portConfigPort=_PortConfigPort_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,2),_PortConfigPort_Type())
portConfigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigPort.setStatus(_A)
_PortConfigLineSpeed_Type=LineSpeed
_PortConfigLineSpeed_Object=MibTableColumn
portConfigLineSpeed=_PortConfigLineSpeed_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,3),_PortConfigLineSpeed_Type())
portConfigLineSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigLineSpeed.setStatus(_A)
_PortConfigDuplex_Type=DuplexSetting
_PortConfigDuplex_Object=MibTableColumn
portConfigDuplex=_PortConfigDuplex_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,4),_PortConfigDuplex_Type())
portConfigDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigDuplex.setStatus(_A)
_PortConfigAutoNeg_Type=AutoNegotiation
_PortConfigAutoNeg_Object=MibTableColumn
portConfigAutoNeg=_PortConfigAutoNeg_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,5),_PortConfigAutoNeg_Type())
portConfigAutoNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigAutoNeg.setStatus(_A)
_PortConfigShutdown_Type=EnabledOrNot
_PortConfigShutdown_Object=MibTableColumn
portConfigShutdown=_PortConfigShutdown_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,6),_PortConfigShutdown_Type())
portConfigShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigShutdown.setStatus(_A)
_PortConfigLoopback_Type=EnabledOrNot
_PortConfigLoopback_Object=MibTableColumn
portConfigLoopback=_PortConfigLoopback_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,7),_PortConfigLoopback_Type())
portConfigLoopback.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigLoopback.setStatus(_A)
_PortConfigFailover_Type=FailoverAction
_PortConfigFailover_Object=MibTableColumn
portConfigFailover=_PortConfigFailover_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,8),_PortConfigFailover_Type())
portConfigFailover.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigFailover.setStatus(_A)
_PortConfigLDSMode_Type=LinkDownMode
_PortConfigLDSMode_Object=MibTableColumn
portConfigLDSMode=_PortConfigLDSMode_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,9),_PortConfigLDSMode_Type())
portConfigLDSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigLDSMode.setStatus(_A)
_PortConfigLDSTimeout_Type=Unsigned32
_PortConfigLDSTimeout_Object=MibTableColumn
portConfigLDSTimeout=_PortConfigLDSTimeout_Object((1,3,6,1,4,1,10734,3,3,2,4,1,1,10),_PortConfigLDSTimeout_Type())
portConfigLDSTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigLDSTimeout.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'LineSpeed':LineSpeed,'DuplexSetting':DuplexSetting,'AutoNegotiation':AutoNegotiation,'EnabledOrNot':EnabledOrNot,'FailoverAction':FailoverAction,'LinkDownMode':LinkDownMode,'tpt-port-config-objs':tpt_port_config_objs,'portConfigTable':portConfigTable,'portConfigEntry':portConfigEntry,_E:portConfigSlot,_F:portConfigPort,'portConfigLineSpeed':portConfigLineSpeed,'portConfigDuplex':portConfigDuplex,'portConfigAutoNeg':portConfigAutoNeg,'portConfigShutdown':portConfigShutdown,'portConfigLoopback':portConfigLoopback,'portConfigFailover':portConfigFailover,'portConfigLDSMode':portConfigLDSMode,'portConfigLDSTimeout':portConfigLDSTimeout})