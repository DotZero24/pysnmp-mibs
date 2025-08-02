_L='NotificationType'
_K='dsx3LineStatus'
_J='dsx3LineIndex'
_I='dsx3IfIndex'
_H='dsx1LineStatus'
_G='dsx1LineIndex'
_F='dsx1IfIndex'
_E='sysUpTime'
_D='sysDescr'
_C='RFC1407-MIB'
_B='RFC1406-MIB'
_A='SNMPv2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,extremenetworks=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent','extremenetworks')
dsx1IfIndex,dsx1LineIndex,dsx1LineStatus=mibBuilder.importSymbols(_B,_F,_G,_H)
dsx3IfIndex,dsx3LineIndex,dsx3LineStatus=mibBuilder.importSymbols(_C,_I,_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysDescr,sysUpTime=mibBuilder.importSymbols(_A,_D,_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_L,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wanDsx1LineStatusChange=NotificationType((1,3,6,1,4,1,1916,0,100))
wanDsx1LineStatusChange.setObjects(*((_A,_E),(_A,_D),(_B,_G),(_B,_F),(_B,_H)))
if mibBuilder.loadTexts:wanDsx1LineStatusChange.setStatus('')
wanDsx1LossOfMasterClock=NotificationType((1,3,6,1,4,1,1916,0,101))
wanDsx1LossOfMasterClock.setObjects(*((_A,_E),(_A,_D),(_B,_G),(_B,_F),(_B,_H)))
if mibBuilder.loadTexts:wanDsx1LossOfMasterClock.setStatus('')
wanDsx1NoLossOfMasterClock=NotificationType((1,3,6,1,4,1,1916,0,102))
wanDsx1NoLossOfMasterClock.setObjects(*((_A,_E),(_A,_D),(_B,_G),(_B,_F),(_B,_H)))
if mibBuilder.loadTexts:wanDsx1NoLossOfMasterClock.setStatus('')
wanDsx3LineStatusChange=NotificationType((1,3,6,1,4,1,1916,0,103))
wanDsx3LineStatusChange.setObjects(*((_A,_E),(_A,_D),(_C,_J),(_C,_I),(_C,_K)))
if mibBuilder.loadTexts:wanDsx3LineStatusChange.setStatus('')
wanDsx3LossOfMasterClock=NotificationType((1,3,6,1,4,1,1916,0,104))
wanDsx3LossOfMasterClock.setObjects(*((_A,_E),(_A,_D),(_C,_J),(_C,_I),(_C,_K)))
if mibBuilder.loadTexts:wanDsx3LossOfMasterClock.setStatus('')
wanDsx3NoLossOfMasterClock=NotificationType((1,3,6,1,4,1,1916,0,105))
wanDsx3NoLossOfMasterClock.setObjects(*((_A,_E),(_A,_D),(_C,_J),(_C,_I),(_C,_K)))
if mibBuilder.loadTexts:wanDsx3NoLossOfMasterClock.setStatus('')
mibBuilder.exportSymbols('WAN-TRAP-MIB',**{'wanDsx1LineStatusChange':wanDsx1LineStatusChange,'wanDsx1LossOfMasterClock':wanDsx1LossOfMasterClock,'wanDsx1NoLossOfMasterClock':wanDsx1NoLossOfMasterClock,'wanDsx3LineStatusChange':wanDsx3LineStatusChange,'wanDsx3LossOfMasterClock':wanDsx3LossOfMasterClock,'wanDsx3NoLossOfMasterClock':wanDsx3NoLossOfMasterClock})